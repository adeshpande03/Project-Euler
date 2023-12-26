def main():
    il = []

    def pow5(n):
        return n**5

    for i in range(2, 1000000):
        if sum(map(pow5, map(int, list(str(i))))) == i:
            il.append(i)
    print(sum(il))


if __name__ == "__main__":
    main()
