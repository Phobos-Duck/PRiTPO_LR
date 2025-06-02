def min_cutting_cost(A, cuts):
    cuts = [0] + cuts + [A]
    n = len(cuts)

    dp = [[0] * n for _ in range(n)]

    for length in range(2, n):
        for i in range(n - length):
            j = i + length
            dp[i][j] = float('inf')
            for k in range(i + 1, j):
                cost = dp[i][k] + dp[k][j] + cuts[j] - cuts[i]
                if cost < dp[i][j]:
                    dp[i][j] = cost
    return dp[0][n - 1]


def main():
    input_data = """100
3
25 50 75
10
4
4 5 7 8
0"""

    lines = [line.strip() for line in input_data.split('\n') if line.strip()]
    idx = 0
    results = []

    while idx < len(lines):
        A = int(lines[idx])
        idx += 1
        if A == 0:
            break

        B = int(lines[idx])
        idx += 1
        cuts = list(map(int, lines[idx].split()))
        idx += 1

        cost = min_cutting_cost(A, cuts)
        results.append(f"The minimum cutting price is {cost}.")

    for result in results:
        print(result)


if __name__ == "__main__":
    main()