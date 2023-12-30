from math import log
from pprint import pprint


def main():
    f = open("./supplements/0099_base_exp.txt").read().splitlines()
    largestLineNum = 0
    f = [list(map(int, list(i.split(",")))) for i in f]
    f = [(i, i[1] * log(i[0])) for i in f]
    for line in range(len(f)):
        if f[line][-1] > f[largestLineNum][-1]:
            largestLineNum = line

    pprint(largestLineNum + 1)


main()
