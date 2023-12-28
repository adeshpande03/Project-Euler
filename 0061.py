from euler_utils import (
    generateTriangularList,
    generateHexagonallList,
    generatePentagonalList,
    generateHeptagonalList,
    generateOctagonalList,
    generateSquareList,
)
from itertools import permutations


def main():
    t = generateTriangularList(150)
    s = generateSquareList(102)
    p = generatePentagonalList(85)
    h = generateHexagonallList(75)
    hp = generateHeptagonalList(65)
    o = generateOctagonalList(60)
    t = [str(i) for i in t]
    s = [str(i) for i in s]
    p = [str(i) for i in p]
    h = [str(i) for i in h]
    hp = [str(i) for i in hp]
    o = [str(i) for i in o]

    def checkInOrder(*args):
        il = []
        l1, l2, l3, l4, l5, l6 = args
        for idx1, l1i in enumerate(l1):
            if len(l1i) != 4:
                continue
            lastTwo = l1i[-2:]
            if lastTwo[0] != "0":
                for idx2, l2i in enumerate(l2):
                    if len(l2i) != 4:
                        continue
                    if l2i.startswith(lastTwo):
                        lastTwo = l2i[-2:]
                        if lastTwo[0] != "0":
                            for idx3, l3i in enumerate(l3):
                                if len(l3i) != 4:
                                    continue
                                if l3i.startswith(lastTwo):
                                    lastTwo = l3i[-2:]
                                    if lastTwo[0] != "0":
                                        for idx4, l4i in enumerate(l4):
                                            if len(l4i) != 4:
                                                continue
                                            if l4i.startswith(lastTwo):
                                                lastTwo = l4i[-2:]
                                                if lastTwo[0] != "0":
                                                    for idx5, l5i in enumerate(l5):
                                                        if len(l5i) != 4:
                                                            continue
                                                        if l5i.startswith(lastTwo):
                                                            lastTwo = l5i[-2:]
                                                            if lastTwo[0] != "0":
                                                                for (
                                                                    idx6,
                                                                    l6i,
                                                                ) in enumerate(l6):
                                                                    if len(l6i) != 4:
                                                                        continue
                                                                    if l6i.startswith(
                                                                        lastTwo
                                                                    ):
                                                                        lastTwo = l6i[
                                                                            -2:
                                                                        ]
                                                                        if l1i.startswith(
                                                                            lastTwo
                                                                        ):
                                                                            s = {
                                                                                idx1,
                                                                                idx2,
                                                                                idx3,
                                                                                idx4,
                                                                                idx5,
                                                                                idx6,
                                                                            }
                                                                            if (
                                                                                len(s)
                                                                                == 6
                                                                            ):
                                                                                il.append(
                                                                                    (
                                                                                        l1i,
                                                                                        l2i,
                                                                                        l3i,
                                                                                        l4i,
                                                                                        l5i,
                                                                                        l6i,
                                                                                    )
                                                                                )
        return il

    for i in permutations([t, s, p, h, hp, o]):
        cO = checkInOrder(*i)
        if cO:
            cO = [str(i) for i in cO[0]] + [str(cO[0][0])]
            if all([cO[i].startswith(cO[i - 1][-2:]) for i in range(1, len(cO))]):
                break
    print(sum(map(int, list(cO[:-1]))))


main()
