from fractions import Fraction


def main():
    c = set()
    for d in range(1, 12001):
        for n in range(d // 2 + 1):
            if n * 3 < d:
                continue
            c.add(Fraction(n, d))
    c = list(sorted(c))
    print(len(c) - c.index(Fraction(1, 3)) - 2)


main()
