from math import factorial
from functools import cache


@cache
def fact(n):
    return factorial(n)


def main():
    il = []
    for i in range(3, 100000):
        c = 0
        for n in str(i):
            c += factorial(int(n))
        b = c == i
        if b:
            il.append(c)
    print(sum(il))


main()
