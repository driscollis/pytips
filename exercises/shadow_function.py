# What's wrong with this code?

import math

def math(*args):
    return sum(args)

def main(number):
    print(f"The square root of {number} if {math.sqrt(number)}")

main(8)