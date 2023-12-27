from euler_utils import createSpiral, listPrimes2, print_justified, isPrime
from pprint import pprint


def main():
    i = 3
    numPrimes = 3
    n = 4
    while True:
        if numPrimes/n < .1:
            print(i - 2)
            break    
        i += 2
        n += 4
        if isPrime(i**2):
            numPrimes += 1
        if isPrime(i**2 - i + 1):
            numPrimes += 1
        if isPrime(i**2 - 2 * i + 2):
            numPrimes += 1
        if isPrime(i**2 - 3 * i + 3):
            numPrimes += 1  
main()
