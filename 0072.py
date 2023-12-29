from euler_utils import gcd
from fractions import Fraction


def main():
    il = [i for i in range(10**6 + 1)]
    s = 0
    for i in range(2, 10**6 + 1):
        if il[i] == i:
            for j in range(i, 10**6 + 1, i):
                il[j] = il[j] / (i) * (i - 1)
        s += il[i]
    print(s)


main()
