# Problem description: https://www.hackerrank.com/challenges/no-idea/problem
from collections import Counter


def get_happiness_score(array: list[int], a: list[int], b: list[int]) -> int:
    happinness_score = 0
    cnt_a, cnt_b = Counter(a), Counter(b)

    for element in array:
        if cnt_a.get(element, None):
            happinness_score += cnt_a[element]
        elif cnt_b.get(element, None):
            happinness_score -= cnt_b[element]

    return happinness_score


if __name__ == "__main__":
    assert get_happiness_score([1, 5, 3], [3, 1], [5, 7]) == 1
