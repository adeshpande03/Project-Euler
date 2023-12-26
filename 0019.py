def main():
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = 1
    sunday_count = 0

    for year in range(1900, 2000):
        for m in months:
            day += m
            if year % 4 == 0 and m == 28:
                day += 1
            if day % 7 == 0:
                sunday_count += 1

    print(sunday_count)


main()
