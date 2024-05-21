from sympy import primefactors
from numpy import prod
def main():
    a = []
    for i in range(1, 100001):
        a.append([i, prod(primefactors(i))])
    a.sort(key = lambda x: x[1])
    print(a[10000 - 1])
    
main()