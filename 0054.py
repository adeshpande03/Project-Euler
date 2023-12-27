from pprint import pprint
from euler_utils import pokerSort, analyzeHand, compareHand


def main():
    f = open("./supplements/0054_poker.txt").read().splitlines()
    f = [[i[:14].strip().split(), i[14:].strip().split()] for i in f]

    s = 0
    for i in f:
        if analyzeHand(i[0])[1] == 4:
            print(i)
            break
        s += compareHand(i[0], i[1])
    print(s)


main()
