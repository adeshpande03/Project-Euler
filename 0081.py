def main():
    f = open("supplements/0081_matrix.txt", "r")
    f = f.readlines()
    f = [list(map(int, line.split(","))) for line in f]
    matrix = f
    m, n = len(f), len(f)
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = matrix[0][0]
    for j in range(1, m):
        dp[0][j] = dp[0][j - 1] + matrix[0][j]
    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + matrix[i][0]
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = matrix[i][j] + min(
                dp[i - 1][j],
                dp[i][j - 1]
            )

    print(dp[-1][-1])


            
        
    
    
    
main()
