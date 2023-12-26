def main():
    fn = 1
    fd = 1
    for num in range(10, 100):
        for den in range(num, 100):
            c = num / den
            if c < 1:
                sn = str(num)
                sd = str(den)
                if sd[-1] == "0" or sn[-1] == "0":
                    continue
                intersection = set(sn).intersection(set(sd))
                if len(set(sn).union(set(sd))) == 3:
                    n = (
                        int(list(set(sn) - intersection)[0])
                        if len(set(sn) - intersection) != 0
                        else int(sn[0])
                    )
                    d = (
                        int((list(set(sd) - intersection)[0]))
                        if len(set(sd) - intersection) != 0
                        else int(sd[0])
                    )
                    if n / d == c:
                        fn *= n
                        fd *= d
    print(fn / fd)


main()
