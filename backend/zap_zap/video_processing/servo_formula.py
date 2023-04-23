import math

h = 640 / 2
w = 480 / 2

H = 60
W = 45

x0 = -118   # distance btwn cameras
ref = 90    # distance s.t. 3x4 board fills image
dx = 92     # distance btwn right cam and servo

def get_servo_space_coord(i1: int, j1: int, i2: int, j2: int):
    b = h - i1
    a = j1 - w

    a1 = H / h * a
    b1 = ref
    c1 = H / h * b

    b = h - i2
    a = j2 - w

    a2 = H / h * a
    b2 = ref
    c2 = H / h * b

    # Phone
    b2x0 = b2 * x0
    denom = a1 * b2 - a2 * b1
    x = a1 * b2x0 / denom
    y = b1 * b2x0 / denom
    z = c1 * b2x0 / denom

    print(f"phone: {(x, y, z)}")

    xs = -y
    ys = x - dx
    zs = z

    return (xs, ys, zs)

eps = 1e-6


def chk_div(num: float, denom: float):
    return num / denom if abs(denom) > eps else None


def servo_params(d: float):

    def solve_angles(x: float, y: float, z: float):
        a = x ** 2 + y ** 2
        b = -2 * d * x
        c = d ** 2 - y ** 2
        disc = math.sqrt(b ** 2 - 4 * a * c)

        cos_theta = (-b - disc) / (2 * a)

        if cos_theta < -1 or 1 < cos_theta:
            cos_theta = (-b + disc) / (2 * a)

        def get_angles(cos_theta):
            theta = math.acos(cos_theta)
            phi = math.atan(z * math.sin(theta) / (d * cos_theta - x))
            return theta, phi

        theta, phi = get_angles(cos_theta)

        if verify_angles(theta, phi, x, y, z):
            return theta, phi
        else:
            return get_angles((-b + disc) / (2 * a))

    def verify_angles(theta: float, phi: float, x: float, y: float, z: float):
        cos_theta = math.cos(theta)
        sin_theta = math.sin(theta)
        cos_phi = math.cos(phi)
        sin_phi = math.sin(phi)

        vterms = (chk_div(x - d * cos_theta, -sin_theta * cos_phi),
                  chk_div(y - d * sin_theta, cos_theta * cos_phi),
                  chk_div(z, sin_phi))

        vterms = tuple(filter(lambda x: x is not None, vterms))

        return all(map(lambda x: abs(x - vterms[0]) < eps, vterms))

    return solve_angles


solve_angles = servo_params(35)