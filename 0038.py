def main():
    il = []
    n = set("123456789")
    for i in range(3, 100000):
        s = ""
        j = 1
        while len(s) < 9:
            s += str(i * j)
            j += 1
        if len(s) == 9 and set(s) == n:
            il.append(int(s))

    print(max(il))


main()
