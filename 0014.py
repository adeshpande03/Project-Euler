from functools import *


@cache
def c(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        if n % 2:
            return 1 + c(3 * n + 1)
        else:
            return 1 + c(n // 2)


def main():
    m = 0
    cm = 0
    for i in range(1000001):
        if c(i) > cm:
            cm = c(i)
            m = i

    print(m)


if __name__ == "__main__":
    main()
