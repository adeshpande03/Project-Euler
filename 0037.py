from euler_utils import isPrime, listPrimes, findNextPrime


def main():
    prime = 11
    il = []
    while len(il) != 11:
        s = str(prime)
        if (all(map(isPrime, [int(s[i:]) for i in range(len(s))]))) and (
            (all(map(isPrime, [int(s[:i]) for i in range(len(s), 0, -1)])))
        ):
            il.append(prime)
        prime = findNextPrime(prime)
    print(sum(il))


main()
