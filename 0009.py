import math
def main():
    a = 3
    b = 4
    for a in range(3, 500):
        for b in range(4, 500):
            c2 = a**2 + b**2
            if math.sqrt(c2)%1 == 0:
                c = math.sqrt(c2)
                if a + b + c == 1000:
                    print(a * b * c)
                    return
        
main()