from euler_utils import listPrimes2, isPrime
from collections import Counter


def main():
    p = listPrimes2(10**6)
    p = [x for x in p if len(str(x)) - len(set(str(x))) >= 3]

    def pdr(s):
        s = str(s)
        sol = []
        for duplicate in Counter(s) - Counter(set(s)):
            a = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
            temp = [int(s.replace(duplicate, x)) for x in a]
            sol.append(temp)
        return sol

    checked = []

    def check(l):
        for i in l:
            checked.append(i)
            if i not in p:
                l.remove(i)
        return l

    flag = True
    i = 0
    while flag:
        if p[i] not in checked:
            replacements = pdr(p[i])
            for j in replacements:
                if len(check(j)) == 8:
                    print(j[0])
                    flag = False
                    break
        i += 1


main()
