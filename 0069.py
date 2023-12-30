from euler_utils import listPrimes2


def main():
    p = listPrimes2(10**7)
    ceiling = 1000000
    result = 1
    for prime in p:
        if result * prime > ceiling:
            print(result)
            return
        result *= prime


main()
