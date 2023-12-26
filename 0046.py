from euler_utils import isPrime, listPrimes, findNextPrime


def main():
    primes = listPrimes(10000)
    pset = set(primes)
    s = set()
    for i in range(3, 10000, 2):
        if i in pset:
            continue
        for q in range(100):
            if i - 2 * q**2 in pset:
                break
            if i - 2 * q**2 < 0:
                print(i)
                return


main()
