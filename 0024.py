from functools import *
import math
from itertools import *

import euler_utils as utils


def main():
    s = "0123456789"
    l = list(permutations(s))
    l.sort()
    print("".join(l[1000000 - 1]))


if __name__ == "__main__":
    main()
