from pprint import pprint


def main(n):
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    dp = [[1] + [0] * (len(coins) - 1) for _ in range(n + 2)]
    for i in range(n + 2):
        for j in range(1, len(coins)):
            if i > coins[j]:
                dp[i][j] += dp[i][j - 1]
                dp[i][j] += dp[i - coins[j]][j]
            else:
                dp[i][j] = dp[i][j - 1]

    for i in dp:
        print(i)


main(200)
