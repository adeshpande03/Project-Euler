from euler_utils import isPrime, findNextPrime, listPrimes


def main():
    l = listPrimes(10000)
    l = [i for i in l if i > 1000]


main()
