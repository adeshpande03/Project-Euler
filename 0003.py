import math


def main(n):
    f = set()
    while n % 2 == 0:
        f.add(2)
        n = n // 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            f.add(i)
            n = n // i
    if n > 2:
        f.add(n)
    print(max((f)))


if __name__ == "__main__":
    main(600851475143)
