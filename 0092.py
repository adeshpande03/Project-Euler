from functools import cache


def main():
    @cache
    def squareSum(num):
        c = 0
        for i in str(num):
            c += int(i) ** 2
        return c

    c = 0
    for num in range(1, 10**7 + 1):
        while True:
            if num != 89 and num != 1:
                num = squareSum(num)
            elif num == 89:
                c += 1
                break
            elif num == 1:
                break
    print(c)


main()
