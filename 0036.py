from euler_utils import isPali


def main():
    s = 0
    for i in range(1, 10**6):
        b = bin(i)[2:]
        if isPali(b) and isPali(i):
            s += i
    print(s)


main()
