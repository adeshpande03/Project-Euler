import math
from functools import cache



def getDiv(n):
    f = set()
    for i in range(1, math.isqrt(n) + 1):
        if n % i == 0:
            f.add(i)
            f.add(n // i)
    return len(f)


def main():
    for i in range(1000000):
        i = i * (i + 1) // 2
        if getDiv(i) > 500:
            print(i)
            break


main()
