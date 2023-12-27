from euler_utils import isPrime, listPrimes


def main():
    primes = listPrimes(1000001)
    pset = set(primes)
    rm = 0
    for i in range(len(primes) - 1, 1, -1):
        for j in range(i):
            if sum(primes[j:i]) > primes[-1]:
                break
            if sum(primes[j:i]) in pset and i - j > rm:
                rm = i - j
                print(sum(primes[j:i]), i - j)


main()
