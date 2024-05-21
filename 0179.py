from sympy import divisor_count
from functools import cache
from tqdm import tqdm


def main():
    @cache
    def d(n):
        return divisor_count(n)
    c = 0
    for n in tqdm(range(1, 10**7)):
        if d(n) == d(n + 1):
            c += 1
    print(c)
       


main()
