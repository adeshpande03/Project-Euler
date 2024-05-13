def main():
    def countNumSums(n):
        num= [0] * (n + 1)
        num[0] = 1
        for i in range(1, n):
            for j in range(i, n + 1):
                num[j] += num[j - i]

        return num[n]
    print(countNumSums(100))
main()
