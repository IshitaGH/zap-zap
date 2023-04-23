#!/usr/bin/env python3

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
