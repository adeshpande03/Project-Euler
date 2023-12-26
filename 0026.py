from functools import cache


def main():
    def cycle(d):
        if d == 0:
            return 0
        n = 1
        reminders = []
        rems = None
        while rems not in reminders:
            reminders.append(rems)
            n *= 10
            rems = n % d
        reminders.pop(0)
        return len(reminders)

    m = 0
    n = 0
    for i in range(1000):
        if cycle(i) > m:
            m = max(m, cycle(i))
            n = i
    print(n)


if __name__ == "__main__":
    main()
