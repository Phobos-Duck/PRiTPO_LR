from collections import defaultdict


def australian_voting(candidates, ballots):
    """
    Функция подсчета голосов кандидатов

    :param candidates: словарь кандидатов
    :param ballots: список бюллетеней
    """
    while True:
        vote_count = defaultdict(int)

        for ballot in ballots:
            if ballot:
                vote_count[ballot[0]] += 1

        total_votes = sum(vote_count.values())
        for candidate, votes in vote_count.items():
            if votes > total_votes / 2:
                return [candidates[candidate]]

        min_votes = min(vote_count.values())
        min_candidates = [cand for cand, votes in vote_count.items() if votes == min_votes]

        if len(min_candidates) == len(vote_count):
            return [candidates[cand] for cand in sorted(vote_count.keys())]

        for cand in min_candidates:
            del candidates[cand]

        new_ballots = []
        for ballot in ballots:
            new_ballot = [vote for vote in ballot if vote in candidates]
            if new_ballot:
                new_ballots.append(new_ballot)

        ballots = new_ballots


def main():
    """
    Функция сортировки входных данных и вывод результата голосования

    :return: Результат голосования
    """
    test_cases = int(input().strip())
    input()
    results = []

    for _ in range(test_cases):
        num_candidates = int(input().strip())

        candidates = {}
        for i in range(1, num_candidates + 1):
            candidates[i] = input().strip()

        ballots = []
        while True:
            try:
                line = input().strip()
                if not line:
                    break
                ballots.append(list(map(int, line.split())))
            except EOFError:
                break

        results.append('\n'.join(australian_voting(candidates.copy(), ballots)))

    print('\n\n'.join(results))


if __name__ == "__main__":
    main()
