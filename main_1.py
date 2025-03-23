def find_min_power_of_2(prefix: str) -> int:
    power = 0
    while True:
        power_of_2 = str(2 ** power)
        if power_of_2.startswith(prefix):
            if len(prefix) < len(power_of_2) - len(prefix):
                return power
        power += 1
        if power > 10000:
            return "no power of 2"


def main():
    inputs = input().strip().split()
    results = [find_min_power_of_2(n) for n in inputs]
    print(" ".join(map(str, results)))


if __name__ == "__main__":
    main()
