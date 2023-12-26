from collections import defaultdict
from math import sqrt


def main():
    d = defaultdict(int)
    for a in range(1, 500):
        for b in range(1, 500):
            cSquared = a**2 + b**2
            if (c := sqrt(cSquared)) % 1 == 0:
                print(a, b, c)
                d[a + b + c // 1] += 1
    m = 0
    c = 0
    for i in d:
        if d[i] > m:
            m = d[i]
            c = i
    print(c)


main()
