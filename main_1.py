def common_sorted_substring(a, b):
    """
    Обрабатывает и сортирует строки входных данных

    :param a: первая строчка данных
    :param b: следующая строчка после a (пара 1+2, 3+4 и т.д)
    :return: находит все x в строчках
    """
    count_a = {}
    count_b = {}

    for char in a:
        count_a[char] = count_a.get(char, 0) + 1
    for char in b:
        count_b[char] = count_b.get(char, 0) + 1

    common_chars = []
    for char in sorted(set(a) & set(b)):
        common_chars.append(char * min(count_a[char], count_b[char]))

    return "".join(common_chars)


def main():
    """
    Считывает входные данные и выводит результат в консоль
    """
    input_lines = []
    while True:
        try:
            line = input().strip()
            if line == "":
                if not input_lines or input_lines[-1] == "":
                    break
            input_lines.append(line)
        except EOFError:
            break

    for i in range(0, len(input_lines), 2):
        if i + 1 < len(input_lines):
            a = input_lines[i]
            b = input_lines[i + 1]
            print(common_sorted_substring(a, b))


if __name__ == "__main__":
    main()