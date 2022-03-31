#!/usr/bin/env python3

# Created by Devin Jhu
# Created on March 2022
# The area calculator

import constants


def main():
    # this function calculates the area of an ellipse

    # input
    print("Ellipse area calculater")
    A = int(input("Enter Axis A(mm): "))
    B = int(input("Enter Axis B(mm): "))

    # process
    area_of_ellipes = A * B * constants.pi

    # output
    print("")
    print("Area is {0} mm².".format(area_of_ellipes))
    print("\nDone.")


if __name__ == "__main__":
    main()
