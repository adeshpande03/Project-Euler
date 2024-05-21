from fractions import Fraction
import sys


def main():
    sys.setrecursionlimit(5000)
    var = 1
    s = "2"
    repStr = f" + Fraction(1, {var})"
    twoIndex = 0
    t = str(eval(s))
    c = 1
    for n in range(99):
        if n % 3 == 1:
            var = 2 * c
            c += 1
        else:
            var = 1
        repStr = f" + Fraction(1, {var})"
        if n == 0:
            s = s + repStr
        else:
            s = s[:twoIndex] + repStr + s[twoIndex:]
        twoIndex -= 1
        t = str(eval(s))
    print(sum(map(int, list(str(t).split("/")[0]))))

main()
