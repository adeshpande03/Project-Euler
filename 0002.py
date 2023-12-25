def main():
    r = [1, 1]
    while r[-1] + r[-2] <= 4 * 10**6:
        r.append(r[-1] + r[-2])
    print(sum([i for i in r if i % 2 == 0]))


if __name__ == "__main__":
    main()
