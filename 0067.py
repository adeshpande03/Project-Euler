def main():
    f = open("./supplements/0067_triangle.txt").read().splitlines()
    f = [list(map(int, i.split())) for i in f]
    current_sums = []
    for row in f:
        len_previous = len(current_sums)
        current_sums = [
            max(
                0 if pos >= len_previous else current_sums[pos],
                current_sums[pos - 1] if 0 < pos <= len_previous else 0,
            )
            + cell_value
            for pos, cell_value in enumerate(row)
        ]

    print(max(current_sums))


main()
