from math import isqrt, sqrt


def main():
    def generatePeriod(num):
        a_n = a_0 = isqrt(num)
        mn, dn = 0, 1
        period = 0
        if a_0 != sqrt(num):
            while a_n != 2 * a_0:
                mn = dn * a_n - mn
                dn = (num - mn**2) / dn
                a_n = int((a_0 + mn) / dn)
                period += 1
        return period
    c = 0
    for i in range(1, 10**4):
        if generatePeriod(i) % 2 == 1:
            c += 1
    print(c)


main()
