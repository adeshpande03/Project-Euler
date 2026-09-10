from math import comb

def main():
    def count_triangles(m, n):
        ans = (m + 1) * m * (n + 1) * n // 4
        return ans
    il = []    
    for i in range(1, 2000):
        for j in range(1, i):
            if 1_500_000 < count_triangles(i, j) < 2_000_010:
                il.append([count_triangles(i, j), i * j])
    il.sort()
    print(il)
    #2772 



main()
