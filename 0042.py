from euler_utils import triangularNumberListGenerator


def main():
    f = open("./supplements/0042_words.txt").read().split(",")
    f = [i[1:-1].lower() for i in f]
    f = [sum([ord(i) - 96 for i in word]) for word in f]
    c = 0
    s = set(triangularNumberListGenerator(1000000))
    for i in f:
        if i in s:
            c += 1
    print(c)


main()
