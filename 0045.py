from euler_utils import (
    generateTriangularList,
    generatePentagonalList,
    generateHexagonallList,
)


def main():
    t = set(generateTriangularList(1000000))
    p = set(generatePentagonalList(1000000))
    h = set(generateHexagonallList(1000000))
    print(t.intersection(p).intersection(h))


main()
