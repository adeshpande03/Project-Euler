from math import lcm
def main(n):
    i = list(range(1, n + 1))
    print(lcm(*i))
main(21)