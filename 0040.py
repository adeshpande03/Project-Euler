def main():
    n = "".join([str(i) for i in range(500000)])
    s = 1
    nums = [10**n for n in range(7)]
    print(nums)
    for c in nums:
        print(n[c])
        s *= int(n[c])
    print(s)


main()
