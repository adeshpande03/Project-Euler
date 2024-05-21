def main():
    bouncyCount = 0

    def isIncreasing(num):
        n = str(num)
        incNum = str("".join(sorted(n)))
        return incNum == n

    def isDecreasing(num):
        n = str(num)
        decNum = str("".join(sorted(n)))[::-1]
        return decNum == n

    def isBouncy(num):
        return (not isDecreasing(num)) and (not isIncreasing(num))

    num = 1
    while True:
        num += 1
        if isBouncy(num):
            bouncyCount += 1
        if bouncyCount == num * 0.99:
            print(num)
            break


main()
