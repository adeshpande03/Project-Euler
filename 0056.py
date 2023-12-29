def main():
    m = 0
    for a in range(100):
        for b in range(100):
            c = 0
            n = str(a**b)
            for num in n:
                c += int(num)
            m = max(m, c)
    print(m)


main()
