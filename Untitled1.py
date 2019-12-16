#!/usr/bin/env python3

# Created by: DJ Watson
# Created on: December 2019
# This program passes an array as a parameter

import random


def calculate(numberlist, mininum):

    minimum = numberlist[0]

    for count in numberlist:
        if count < minimum:
            minimum = count
    return minimum


def main():
    # function holds list

    # variables
    numbers = []
    min_number = 0

    # input
    print("numbers are: ")
    for loop_c in range(0, 9):
        single_number = random.randint(0, 100)
        numbers.append(single_number)
        print("{}".format(single_number))
    print("")

    total = calculate(numbers, min_number)

    print("lowest number = {}".format(total))


if __name__ == "__main__":
    main()
