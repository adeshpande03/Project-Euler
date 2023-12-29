from itertools import permutations
from euler_utils import listOfNumsToInt


def main():
    nums = [2, 3, 5, 7, 11, 13, 17]
    il = []
    for i in permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
        i = str(listOfNumsToInt(i))
        if all([int(i[idx : idx + 3]) % nums[idx - 1] == 0 for idx in range(1, 8)]):
            il.append(int(i))
    print(sum(il))


main()
