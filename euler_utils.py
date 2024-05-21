import math
from functools import cache, lru_cache


@cache
def getDiv(n):
    """Returns a list of divisors of n as a sorted list (does not include n)

    Returns:
        list:  divisors of n as a sorted list (does not include n)
    """
    f = set()
    for i in range(1, math.isqrt(n) + 1):
        if n % i == 0:
            f.add(i)
            f.add(n // i)
    return list(sorted(f))


def isPrime(num):
    """checks if num is prime

    Args:
        num (int): num to be checked

    Returns:
        bool: True if num is prime, False if not
    """

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
    """_summary_

    Args:
        num (int): a starting number to find the next prime from

    Returns:
        int: prime after num
    """
    if num < 2:
        return 2
    if num % 2 == 0:
        num -= 1
    guess = num + 2
    while not isPrime(guess):
        guess += 2
    return guess


def listPrimes(maxNum):
    """lists primes until maxNum

    Args:
        maxNum (int): max num to bind the largest prime generated

    Returns:
        list: list of primes <= maxNum
    """
    l = [2]
    while l[-1] < maxNum:
        l.append(findNextPrime(l[-1]))
    return l[:-1]


@cache
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


def isPali(numOrString):
    s = str(numOrString)
    return s == s[::-1]


def listOfNumsToInt(listOfIntsOrStrings):
    res = int("".join(map(str, listOfIntsOrStrings)))
    return res


def generateTriangularList(listLen):
    return [n * (n + 1) // 2 for n in range(1, listLen + 1)]


def generateSquareList(listLen):
    return [((n) * n) for n in range(1, listLen)]


def generatePentagonalList(listLen):
    return [((3 * n - 1) * n) // 2 for n in range(1, listLen)]


def generateHexagonallList(listLen):
    return [((2 * n - 1) * n) for n in range(1, listLen)]


def generateHeptagonalList(listLen):
    return [n * (5 * n - 3) // 2 for n in range(1, listLen + 1)]


def generateOctagonalList(listLen):
    return [((3 * n - 2) * n) for n in range(1, listLen)]


def listPrimes2(num):
    """Sieve of Eratosthenes from geeksforgeeks

    Args:
        num (int): num that binds primes[-1]

    Returns:
        list: list of primes less than num
    """
    prime = [True for i in range(num + 1)]
    p = 2
    primes = []
    while p * p <= num:
        if prime[p] == True:
            for i in range(p * p, num + 1, p):
                prime[i] = False
        p += 1
    for p in range(2, num + 1):
        if prime[p]:
            primes.append(p)
    return primes


def pokerSort(rank):
    order = "23456789TJQKA"
    return order.index(rank)


def analyzeHand(hand):
    order = "23456789TJQKA"
    r = []
    s = []
    for card in hand:
        r.append(card[0])
        s.append(card[1])
    rCount = [r.count(i) for i in r]
    r.sort(key=pokerSort)
    a = 0
    if "".join(r) in order or "".join(r) == "A2345" and 5 in s:
        a = 11
    elif 4 in rCount:
        a = 10
    elif 3 in rCount and 2 in rCount:
        a = 9
    elif 5 in s:
        a = 8
    elif "".join(r) in order or "".join(r) == "A2345":
        a = 7
    elif 3 in rCount and rCount.count(1) == 2:
        a = 6
    elif rCount.count(2) == 4:
        a = 5
    elif rCount.count(2) == 2:
        a = 4
    else:
        a = 3
    return a - 3, r


def compareHand(hand1, hand2):
    r1 = []
    r2 = []
    a1 = analyzeHand(hand1)
    a2 = analyzeHand(hand2)
    if a1[0] > a2[0]:
        return 1
    if a2[0] > a1[0]:
        return 0
    if a1[0] == a2[0]:
        r1 = list(set([(pokerSort(str(i)), a1[1].count(i)) for i in a1[1]]))
        r2 = list(set([(pokerSort(str(i)), a2[1].count(i)) for i in a2[1]]))
        r1.sort(key=lambda x: (x[1], (x[0])), reverse=True)
        r2.sort(key=lambda x: (x[1], (x[0])), reverse=True)
        for idx in range(len(r1)):
            c1 = r1[idx]
            c2 = r2[idx]
            if c1 == c2:
                continue
            if c1[0] > c2[0]:
                return 1
            return 0


def gcd(p, q):
    while q != 0:
        p, q = q, p % q
    return p


def isCoprime(a, b):
    return gcd(a, b) == 1


def totient(n):
    result = 1
    for i in range(2, n):
        if gcd(i, n) == 1:
            result += 1
    return result


def isIncreasing(num):
    n = str(num)
    incNum = str("".join(sorted(n)))
    return incNum == n


def isDecreasing(num):
    n = str(num)
    decNum = str("".join(sorted(n)))[::-1]
    return decNum == n


def isBouncy(num):
    return (not isDecreasing(num)) and (not isIncreasing(num))
