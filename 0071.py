from fractions import Fraction


def main():
    m = 0
    for d in range(10**6, 10**6 - 1000, -1):
        for n in range(d // 2, 0, -1):
            if 100000 * n < d * 42857:
                break
            if 7 * n > d * 3:
                continue
            if Fraction(3, 7) > Fraction(n, d) > m:
                m = Fraction(n, d)

    print(m)


main()
