def flip(stack, k):
    """Переворачивает первые k элементов стопки."""
    return stack[:k][::-1] + stack[k:]


def pancake_sort(stack):
    """Сортирует стопку оладий с помощью переворотов."""
    n = len(stack)
    flips = []

    for size in range(n, 1, -1):
        # Находим индекс самого большого элемента в текущем подмассиве
        max_idx = stack.index(max(stack[:size]))

        if max_idx == size - 1:
            continue

        # Если максимум не на вершине, переворачиваем так, чтобы он оказался сверху
        if max_idx != 0:
            stack = flip(stack, max_idx + 1)
            flips.append(n - max_idx)

        # Переворачиваем, чтобы переместить максимум вниз
        stack = flip(stack, size)
        flips.append(n - size + 1)

    flips.append(0)  # Завершающий ноль
    return flips


def main():
    input_data = []
    while True:
        try:
            line = input().strip()
            if line == "":
                break
            input_data.append(line)
        except EOFError:
            break

    for line in input_data:
        stack = list(map(int, line.split()))
        flips = pancake_sort(stack)
        print(" ".join(map(str, stack)))
        print(" ".join(map(str, flips)))


if __name__ == "__main__":
    main()
