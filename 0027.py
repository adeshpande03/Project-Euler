import euler_utils as utils


def main():
    bList = utils.listPrimes(1000)
    n = 0
    af = 0
    bf = 0
    for b in bList:
        for a in range(-999, 1000):

            def f(x):
                return x**2 + a * x + b

            i = 0
            c = 0
            while utils.isPrime(f(i)):
                c += 1
                i += 1
            if c > n:
                n = c
                af = a
                bf = b
    print(af * bf)


if __name__ == "__main__":
    main()
