from euler_utils import isPrime, findNextPrime, listPrimes
from collections import OrderedDict


def main():
    l = listPrimes(10000)
    l = [(i) for i in l if i > 1000]
    sl = set(l)
    d = OrderedDict()
    for i in l:
        il = []
        if i + 3330 in l and i + 6660 in l:
            il.append(i)
            il.append(i + 3330)
            il.append(i + 6660)

        if il:
            il = [str(i) for i in il]
            s = set(il[0])
            if all([set(i) == s for i in il]):
                print("".join(il))


main()
