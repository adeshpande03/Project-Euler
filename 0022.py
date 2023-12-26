from functools import *
import math


def main():
    ans = 0
    lines = [i[1:-1] for i in open("./supplements/0022_names.txt").read().split(",")]
    lines.sort()
    for j, i in enumerate(lines):
        c = 0
        for d in i.lower():
            c += ord(d) - 96
        ans += c * (j + 1)
    print(ans)

    pass


if __name__ == "__main__":
    main()
