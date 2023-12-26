from euler_utils import isPrime, listPrimes
from collections import deque


def main():
    il = listPrimes(10**6)
    c = 0

    def rotation(n):
        out = []
        n = deque([int(i) for i in list(str(n))])
        for _ in range(len(n)):
            out.append(int("".join([str(i) for i in ((n))])))
            n.rotate()
        return out

    for i in il:
        g = rotation(i)
        if all([isPrime(x) for x in g]):
            c += 1
            print(i)
    print(c)


main()
