def main():
    f = []
    for i in range(999, 101, -1):
        for j in range(999, 101, -1):
            s = str(i * j)
            if s == s[::-1]:
                f.append(int(s))
    print(max(f))
main()