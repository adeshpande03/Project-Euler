def main(n):
    c = 0
    for i in range(n):
        if 0 == i % 3 or 0 == i % 5:
            print(i)
            c += i
    print(c)


if __name__ == "__main__":
    main(1000)
