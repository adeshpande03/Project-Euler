from euler_utils import isPali


def main():
    c = 0
    for num in range(10000):
        for i in range(50):
            num = num + int(str(num)[::-1])
            if isPali(num):
                break
        else:
            c += 1
    print(c)


main()
