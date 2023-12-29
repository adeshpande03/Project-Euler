def main():
    c = 0
    for a in range(1, 100):
        for b in range(1, 100):
            if len(str(a**b)) == b:
                c += 1
    print(c)


main()
