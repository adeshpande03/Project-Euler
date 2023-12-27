from fractions import Fraction
import sys

def main():
    sys.setrecursionlimit(5000)
    s = "1 + Fraction(1, 2)"
    repStr = " + Fraction(1, 2)"
    twoIndex = -1
    c = 0
    for _ in range(1000):
        s = s[:twoIndex] + repStr + s[twoIndex:]
        twoIndex -= 1
        t = str(eval(s))
        t = t.split("/")
        if len(t[0]) > len(t[1]):
            c +=1
    print(c)
main()
