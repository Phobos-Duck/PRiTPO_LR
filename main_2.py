def count_expressions(n, d):
    if n % 2 != 0:
        return 0
    max_n = 300
    max_d = 150
    dp = [[0] * (max_d + 2) for _ in range(max_n + 2)]
    dp[0][0] = 1

    for i in range(2, n + 1, 2):
        for j in range(1, d + 1):
            if i - 2 >= 0 and j - 1 >= 0:
                dp[i][j] += dp[i - 2][j - 1]
            for k in range(2, i, 2):
                for m in range(0, j + 1):
                    if dp[k][m] and dp[i - k][j]:
                        dp[i][j] += dp[k][m] * dp[i - k][j]
                for m in range(0, j):
                    if dp[k][j] and dp[i - k][m]:
                        dp[i][j] += dp[k][j] * dp[i - k][m]
    return dp[n][d]

input_examples = [
    (6, 2),
    (300, 150)
]

for n, d in input_examples:
    result = count_expressions(n, d)
    print(result)