from collections import deque


def solve(input_data):
    lines = [line.strip() for line in input_data.split('\n') if line.strip()]
    ptr = 0

    while ptr < len(lines):
        # Пропускаем пустые строки
        while ptr < len(lines) and not lines[ptr]:
            ptr += 1
        if ptr >= len(lines):
            break

        # Читаем nk и np
        nk, np = map(int, lines[ptr].split())
        ptr += 1
        if nk == 0 and np == 0:
            break

        # Читаем требования по категориям
        while ptr < len(lines) and not lines[ptr]:
            ptr += 1
        requirements = list(map(int, lines[ptr].split()))
        ptr += 1

        # Читаем задачи и их категории
        problems = []
        for _ in range(np):
            while ptr < len(lines) and not lines[ptr]:
                ptr += 1
            if ptr >= len(lines):
                break
            parts = list(map(int, lines[ptr].split()))
            categories = parts[1:]
            problems.append(categories)
            ptr += 1

        # Строим граф
        size = 1 + nk + np + 1
        graph = [[0] * size for _ in range(size)]

        # Исток -> категории
        for i in range(1, nk + 1):
            graph[0][i] = requirements[i - 1]

        # Категории -> задачи
        for j in range(np):
            for cat in problems[j]:
                graph[cat][nk + 1 + j] = 1

        # Задачи -> сток
        for j in range(np):
            graph[nk + 1 + j][nk + np + 1] = 1

        # Алгоритм Диница
        def bfs():
            level = [-1] * size
            q = deque()
            level[0] = 0
            q.append(0)
            while q:
                u = q.popleft()
                for v in range(size):
                    if level[v] == -1 and graph[u][v] > 0:
                        level[v] = level[u] + 1
                        q.append(v)
            return level

        def dfs(u, flow, level, ptr_flow):
            if u == nk + np + 1:
                return flow
            while ptr_flow[u] < size:
                v = ptr_flow[u]
                if v < size and level[v] == level[u] + 1 and graph[u][v] > 0:
                    pushed = dfs(v, min(flow, graph[u][v]), level, ptr_flow)
                    if pushed > 0:
                        graph[u][v] -= pushed
                        graph[v][u] += pushed
                        return pushed
                ptr_flow[u] += 1
            return 0

        max_flow = 0
        while True:
            level = bfs()
            if level[nk + np + 1] == -1:
                break
            ptr_flow = [0] * size
            while True:
                flow = dfs(0, float('inf'), level, ptr_flow)
                if flow == 0:
                    break
                max_flow += flow

        total_required = sum(requirements)
        if max_flow != total_required:
            print(0)
            continue

        print(1)
        solution = [[] for _ in range(nk)]
        for j in range(np):
            for i in range(nk):
                if graph[nk + 1 + j][i + 1] == 1:
                    solution[i].append(j + 1)

        # Вывод решения в требуемом формате
        for category in solution:
            if category:
                print(' '.join(map(str, sorted(category))))
            else:
                print()
        print(0)  # Завершающий 0 как в примере


# Входные данные
input_data = """
3 15
3 3 4
2 1 2
1 3
1 3
1 3
1 3
3 1 2 3
2 2 3
2 1 3
1 2
1 2
2 1 2
2 1 3
2 1 2

1 1
3 1 2 3
3 15
7 3 4
2 1 2
1 1
1 2
1 2
1 3
3 1 2 3 2 2 3
2 2 3
1 2
1 2
2 2 3
2 2 3
2 1 2
1 1
3 1 2 3
0 0
"""

solve(input_data)