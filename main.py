def get_new_deck():
    """
    Создает новую стандартную колоду карт в начальном порядке.
    """
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    return [f"{value} of {suit}" for suit in suits for value in values]


def apply_shuffle(deck, shuffle):
    """
    Применяет трюк к текущей колоде.
    """
    return [deck[i - 1] for i in shuffle]


def main():
    """
    Считывает данные из консоли и выводит их.
    """
    input_data = []
    while True:
        try:
            line = input().strip()
            if line == "":
                if input_data and input_data[-1] == "":
                    break
                input_data.append(line)
            else:
                input_data.append(line)
        except EOFError:
            break

    index = 0
    test_cases = int(input_data[index])
    index += 1
    results = []

    for _ in range(test_cases):
        index += 1
        n = int(input_data[index])
        index += 1

        shuffles = []
        for _ in range(n):
            shuffle = list(map(int, input_data[index].split()))
            if len(shuffle) != 52:
                raise ValueError("Ошибка: В каждом трюке должно быть 52 числа.")
            shuffles.append(shuffle)
            index += 1

        deck = get_new_deck()

        while index < len(input_data) and input_data[index].strip():
            k = int(input_data[index]) - 1
            deck = apply_shuffle(deck, shuffles[k])
            index += 1

        results.append("\n".join(deck))

    print("\n\n".join(results))


if __name__ == "__main__":
    main()