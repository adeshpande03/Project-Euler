def main():
    cubes = ["".join(sorted(str(n**3))) for n in range(0, 10000)]
    for i in cubes:
        if cubes.count(i) == 5:
            print(cubes.index(i) ** 3)
            break


main()
