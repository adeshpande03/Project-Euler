from euler_utils import isPali, listPrimes2
import sys

sys.set_int_max_str_digits(3 * 10**6)


def main():
    c = []
    p = [i**2 for i in listPrimes2(10**7 * 5)]
    pset = set(p)
    for i in p:
        if int(str(i)[::-1]) in pset and not isPali(i):
            c.append(i)
        if len(c) == 50:
            break
    print((sum(c)))


main()
