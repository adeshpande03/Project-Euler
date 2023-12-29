from euler_utils import createSpiral, print_justified
from pprint import pprint


def main(n):
    spiral = createSpiral(n)
    diag1Start = [0, 0]
    diag2Start = [0, -1]
    s = 0
    for _ in range(n):
        oner, onec = diag1Start
        twor, twoc = diag2Start
        s += spiral[oner][onec]
        s += spiral[twor][twoc]
        diag1Start = [oner + 1, onec + 1]
        diag2Start = [twor + 1, twoc - 1]

    s -= 1
    print(s)


if __name__ == "__main__":
    main(9)
