face_names = ['front', 'back', 'left', 'right', 'top', 'bottom']
opposite_face = [1, 0, 3, 2, 5, 4]  # Индексы противоположных граней


def solve(input_data):
    lines = [line.strip() for line in input_data.split('\n') if line.strip()]
    case_number = 0
    index = 0

    while index < len(lines):
        N = int(lines[index])
        if N == 0:
            break
        index += 1

        cubes = []
        for _ in range(N):
            while index < len(lines) and not lines[index].strip():
                index += 1
            if index >= len(lines):
                break
            cube = list(map(int, lines[index].strip().split()))
            if len(cube) != 6:
                print(f"Error: Cube should have 6 faces, got {len(cube)}")
                break
            cubes.append(cube)
            index += 1

        case_number += 1
        process_case(case_number, N, cubes)


def process_case(case_number, N, cubes):
    dp = [[1] * 6 for _ in range(N)]
    prev = [[None] * 6 for _ in range(N)]

    max_height = 1
    last_cube = 0
    last_face = 0

    for i in range(N):
        for j in range(6):
            for k in range(i):
                for m in range(6):
                    if cubes[k][opposite_face[m]] == cubes[i][j]:
                        if dp[k][m] + 1 > dp[i][j]:
                            dp[i][j] = dp[k][m] + 1
                            prev[i][j] = (k, m)
            if dp[i][j] > max_height:
                max_height = dp[i][j]
                last_cube = i
                last_face = j

    result = []
    current_cube, current_face = last_cube, last_face
    while current_cube is not None:
        result.append(f"{current_cube + 1} {face_names[current_face]}")
        prev_info = prev[current_cube][current_face]
        if prev_info is None:
            break
        current_cube, current_face = prev_info

    result.reverse()

    print(f"Case #{case_number}")
    print(max_height)
    for line in result:
        print(line)
    print()

input_data = """
3
1 2 2 2 1 2
3 3 3 3 3 3
3 2 1 1 1 1
10
1 5 10 3 6 5
2 6 7 3 6 9
5 7 3 2 1 9
1 3 3 5 8 10
6 6 2 2 4 4
1 2 3 4 5 6
10 9 8 7 6 5
6 1 2 3 4 7
1 2 3 3 2 1
3 2 1 1 2 3
0
"""

solve(input_data)