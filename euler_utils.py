import math
import functools


def getDiv(n):
    f = set()
    for i in range(1, math.isqrt(n) + 1):
        if n % i == 0:
            f.add(i)
            f.add(n // i)
    return list(sorted(f))


def isPrime(num):
    if num < 2 or num % 2 == 0:
        return num == 2
    divisor = 3
    while divisor <= math.sqrt(num):
        if num % divisor == 0:
            return False
        else:
            divisor += 2
    return True


def findNextPrime(num):
    if num < 2:
        return 2
    if num % 2 == 0:
        num -= 1
    guess = num + 2
    while not isPrime(guess):
        guess += 2
    return guess


def listPrimes(maxNum):
    l = [2]
    while l[-1] < maxNum:
        l.append(findNextPrime(l[-1]))
    return l[:-1]


@functools.cache
def collatz(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        if n % 2:
            return 1 + collatz(3 * n + 1)
        else:
            return 1 + collatz(n // 2)


def twoSumExists(a, l):
    l = l + l
    d = set()
    for i in l:
        if i in d:
            return True
        else:
            d.add(a - i)
    return False


def print_justified(list_of_lists):
    col_widths = [max(len(str(item)) for item in col) for col in zip(*list_of_lists)]

    for row in list_of_lists:
        print(" ".join(str(item).ljust(width) for item, width in zip(row, col_widths)))


def createSpiral(n):
    if n % 2 == 0:
        n += 1
    spiral = [[0 for _ in range(n)] for _ in range(n)]
    (finalVertical, finalHorizontal) = (n // 2, n // 2)
    (vertical, horizontal) = (0, n - 1)
    num = n**2
    directions = {"right": (0, 1), "down": (1, 0), "left": (0, -1), "up": (-1, 0)}
    currDirection = "left"
    while spiral[finalVertical][finalHorizontal] == 0:
        spiral[vertical][horizontal] = num
        if n**2 - 4 * n <= num <= n**2:
            if horizontal + 1 == n and currDirection == "right":
                currDirection = "up"
            elif horizontal == 0 and currDirection == "left":
                currDirection = "down"
            elif vertical + 1 == n and currDirection == "down":
                currDirection = "right"

        if (
            spiral[vertical + directions[currDirection][0]][
                horizontal + directions[currDirection][1]
            ]
            != 0
            and currDirection == "right"
        ):
            currDirection = "up"
        elif (
            spiral[vertical + directions[currDirection][0]][
                horizontal + directions[currDirection][1]
            ]
            != 0
            and currDirection == "left"
        ):
            currDirection = "down"
        elif (
            spiral[vertical + directions[currDirection][0]][
                horizontal + directions[currDirection][1]
            ]
            != 0
            and currDirection == "down"
        ):
            currDirection = "right"
        elif (
            spiral[vertical + directions[currDirection][0]][
                horizontal + directions[currDirection][1]
            ]
            != 0
            and currDirection == "up"
        ):
            currDirection = "left"

        vertical, horizontal = (
            vertical + directions[currDirection][0],
            horizontal + directions[currDirection][1],
        )
        num -= 1
    return spiral
