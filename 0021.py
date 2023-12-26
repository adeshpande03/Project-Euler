from functools import *
import math


def main():
    a = 0

    @cache
    def getDiv(n):
        f = set()
        for i in range(1, math.isqrt(n) + 1):
            if n % i == 0:
                f.add(i)
                f.add(n // i)
        return sum(list(sorted(list(f)))[:-1])

    for i in range(1, (10000)):
        d = getDiv(i)
        e = getDiv(d)
        if e == i and i != d:
            a += i
    print(a)

    pass


if __name__ == "__main__":
    main()
