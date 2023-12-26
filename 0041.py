from euler_utils import isPrime
from itertools import permutations


def main():
    s = "1234567"
    m = 0
    for i in permutations(s, 7):
        if isPrime(int("".join([str(g) for g in i]))):
            m = max(m, int("".join([str(g) for g in i])))
    print(m)


main()
