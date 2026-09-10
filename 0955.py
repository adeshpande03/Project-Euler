from sympy import divisors
def main(p):
    n = 0
    a = 3
    for _ in range(p - 1):
        m = 2 * a
        for x in divisors(m):
            y = m // x
            if (x - y) & 1:
                k = (x - y - 1) // 2
                if k > 0:
                    n += k
                    a += k * (k + 1) // 2
                    break
    return n

print(main(70))