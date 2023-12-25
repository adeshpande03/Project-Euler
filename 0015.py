from functools import *
from pprint import *
def main(n):
    dp = [[1] + [0 for _ in range(n)] for __ in range(n + 1)]
    dp[0] = [1] * len(dp[0])
    for i in range(1, len(dp)):
        for j in range(1, len(dp[i])):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    print(dp[-1][-1])
    
    
if __name__ == "__main__":
    main(20)
