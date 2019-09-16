#!/usr/bin/env python3

# Created by: Teddy Sannan
# Created on: September 2019
# This program calculates the circumfrence of a circle
#    with user input

import constants


def main():
    # This function claculates the circumfrence
    # input
    radius = int(input("Enter radius of a circle (mm): "))
    # process
    circumfrence = constants.TAU*radius
    # output
    print("")
    print("Circumfrence is {}mm^2".format(circumfrence))


if __name__ == "__main__":
    main()
