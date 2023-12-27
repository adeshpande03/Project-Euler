from math import comb


def main():
    c = 0
    for n in range(1, 101):
        for r in range(1, n + 1):
            if comb(n, r) > 10**6:
                c += 1
    print(c)


main()
