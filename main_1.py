def rope_teams(test_cases):
    results = []
    for case in test_cases:
        n, weights = case
        total_weight = sum(weights)
        max_half = (n + 1) // 2
        max_weight = total_weight // 2

        dp = [[0] * (max_weight + 1) for _ in range(max_half + 1)]

        for weight in weights:
            for i in range(max_half, 0, -1):
                for j in range(max_weight, weight - 1, -1):
                    if dp[i - 1][j - weight] + weight > dp[i][j]:
                        dp[i][j] = dp[i - 1][j - weight] + weight

        best_weight = 0
        for i in range(max_half, 0, -1):
            if dp[i][max_weight] > best_weight:
                best_weight = dp[i][max_weight]

        other_weight = total_weight - best_weight
        if best_weight < other_weight:
            results.append(f"{best_weight} {other_weight}")
        else:
            results.append(f"{other_weight} {best_weight}")
    return results

def main():
    input_data = """
    1

    3
    100
    90
    200
    """

    lines = [line.strip() for line in input_data.split('\n') if line.strip()]
    idx = 0
    T = int(lines[idx])
    idx += 1
    test_cases = []
    while idx < len(lines):
        n = int(lines[idx])
        idx += 1
        weights = []
        for _ in range(n):
            weights.append(int(lines[idx]))
            idx += 1
        test_cases.append((n, weights))

    results = rope_teams(test_cases)
    for i, res in enumerate(results):
        print(res)
        if i < len(results) - 1:
            print()


if __name__ == "__main__":
    main()