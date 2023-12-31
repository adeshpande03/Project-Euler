from euler_utils import listPrimes2
from math import isqrt
from itertools import combinations_with_replacement


def main():
    d = 0
    p = listPrimes2(10**8 // 2)
    print()
    for i in range(len(p)):
        for j in range(i, len(p)):
            if p[i] ** 2 > 10**8:
                break
            elif p[i] * p[j] < 10**8:
                d += 1
            else:
                break
    print(d)


main()
