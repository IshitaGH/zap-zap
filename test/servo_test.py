#!/usr/bin/env python3

import struct
import socket
import math

from formula import get_servo_space_coord

ip = input("ip: ")

sock = socket.create_connection((ip, 8000))

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


try:
    while True:
        inp = input("> ")
        match inp.split():
            case ["at", i1, j1, i2, j2]:
                i1 = int(i1)
                j1 = int(j1)
                i2 = int(i2)
                j2 = int(j2)

                x, y, z = get_servo_space_coord(i1, j1, i2, j2)
                print(f"servo: {(x, y, z)}")

                theta, phi = solve_angles(x, y, z)

                # Calibration
                theta += 5.5 * math.pi / 180
                phi -= 7.2 * math.pi / 180

                print(f"theta = {theta} phi = {phi}")

                f1 = theta / math.pi
                f2 = phi / math.pi + 0.5

                msg = struct.pack("!bff", 2, f1, f2)

            case ["on"]:
                msg = struct.pack("!b", 1)

            case ["off"]:
                msg = struct.pack("!b", 0)

            case _:
                print("invalid message")
                continue

        print(msg)
        sock.sendall(msg)

except Exception as e:
    print(e)

finally:
    sock.close()
