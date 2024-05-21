from math import factorial
from tqdm import tqdm
from functools import cache


def main():
    c = 0
    
    @cache
    def factNum(num):
        s = 0
        curNum = num
        while curNum:
            curNum, factNum = curNum // 10, curNum % 10
            s += factorial(factNum)
        return s

    def factChain(num):
        seen = [num]
        curNum = num
        while True:
            s = factNum(curNum)
            if s in seen:
                break
            seen.append(s)
            curNum = s
        return len(seen)
    assert factChain(69) == 5
    for num in tqdm(range(1, 10**6)):
        if factChain(num) == 60:
            c += 1
    print(c)


main()
