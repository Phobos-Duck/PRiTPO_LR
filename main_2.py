def count_lost_workdays(n, parties):
    """
    Рассчет с учетом входных данных кол-ва потерянных рабочих дней
    
    :param n: кол-во дней
    :param parties: список чисел, где каждое p означает, что партия устраивает забастовку каждые эти p дней
    :return: кол-во потерянных рабочих дней
    """
    lost_days = set()

    for p in parties:
        for day in range(p, n + 1, p):
            if day % 7 not in (6, 0):  # Исключаем пятницы (6) и субботы (0)
                lost_days.add(day)

    return len(lost_days)


def main():
    """
    Основная функция считывания и обработки входных данных
    """
    data = list(map(int, input().split()))
    index = 0
    t = data[index]
    index += 1
    results = []

    for _ in range(t):
        n = data[index]
        index += 1
        p = data[index]
        index += 1
        parties = data[index:index + p]
        index += p
        results.append(count_lost_workdays(n, parties))

    for res in results:
        print(res)


if __name__ == "__main__":
    main()
