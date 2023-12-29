from functools import *
import math

import euler_utils as utils


def main():
    il = []
    a = 0
    s = []
    for i in range(1, 28123 + 1):
        if sum(utils.getDiv(i)[:-1]) > i:
            il.append(i)
    for i in range(1, 28123 + 1):
        if not utils.twoSumExists(i, il):
            s.append(i)
    print(sum(s))


if __name__ == "__main__":
    main()
