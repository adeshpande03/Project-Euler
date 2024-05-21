import decimal
from math import isqrt, sqrt


def main():
    c = -1
    decimal.getcontext().prec = 101
    for i in range(1, 101):
        if isqrt(i) == sqrt(i):
            continue
        i = decimal.Decimal(i).sqrt()
        s = str(i)
        print(s)
        s = ''.join(s.split('.')[0]) + ''.join(s.split('.')[1]) 
        s = sum(list(map(int, s[:100])))
        c += s
    print(c)


main()
