from itertools import permutations


def main():
    nums = list("123456789")
    s = set()
    for num in list(permutations(nums, 9)):
        if int("".join(num[:2])) * int("".join(num[2:5])) == int("".join(num[5:])):
            s.add(int("".join(num[5:])))
        elif int("".join(num[:3])) * int("".join(num[3:5])) == int("".join(num[5:])):
            s.add(int("".join(num[5:])))
        elif int("".join(num[:4])) * int("".join(num[4:5])) == int("".join(num[5:])):
            s.add(int("".join(num[5:])))
    print(sum(s))


main()
