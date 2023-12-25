from math import lcm
def main(n):
    i = list(range(1, n + 1))
    print(lcm(*i))
if __name__ == "__main__":
    main(21)
