from euler_utils import findNextPrime, listPrimes2
from tqdm import tqdm

def main():
    primes = listPrimes2(10000001)
    print("Primes done")
    n = 1
    for p in tqdm(primes):
        r = ((p - 1) ** n + (p + 1) ** n) % (p**2)


        if r > 10 ** 10:
            print(n)
            break
        n += 1
        

main()
