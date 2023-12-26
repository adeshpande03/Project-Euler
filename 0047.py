from euler_utils import getDiv
from functools import cache
from sympy.ntheory import factorint


def main():
    for i in range(0, 10000000):
        n1 = i
        n2 = i + 1
        n3 = i + 2
        n4 = i + 3

        s1 = factorint(n1)
        s2 = factorint(n2)
        s3 = factorint(n3)
        s4 = factorint(n4)

        if len(s1) != 4:
            continue
        if len(s2) != 4:
            continue
        if len(s3) != 4:
            continue
        if len(s4) != 4:
            continue
        s = set(
            [(i, s1[i]) for i in s1]
            + [(i, s2[i]) for i in s2]
            + [(i, s3[i]) for i in s3]
            + [(i, s4[i]) for i in s4]
        )
        if len(s) == 16:
            print(i)
            break


main()
