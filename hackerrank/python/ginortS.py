# Problem description: https://www.hackerrank.com/challenges/ginorts/problem
from collections import defaultdict


class CT:
    LOWER_CASE = "lower_case"
    UPPER_CASE = "upper_case"
    DIGITS = "digits"


def parse_and_sort(parts: dict[str, list[str]], ct: str) -> str:
    if ct == CT.DIGITS:
        odd = [x for x in parts[ct] if int(x) % 2 != 0]
        even = [x for x in parts[ct] if int(x) % 2 == 0]

        return "".join(sorted(odd)) + "".join(sorted(even))
    else:
        return "".join(sorted(parts[ct]))


def perform_special_sorting(input_str: str) -> str:
    parts = defaultdict(list)

    for char in input_str:
        if char.islower():
            parts[CT.LOWER_CASE].append(char)
        elif char.isupper():
            parts[CT.UPPER_CASE].append(char)
        elif char.isdigit():
            parts[CT.DIGITS].append(char)

    return (
        f"{parse_and_sort(parts, CT.LOWER_CASE)}"
        f"{parse_and_sort(parts, CT.UPPER_CASE)}"
        f"{parse_and_sort(parts, CT.DIGITS)}"
    )


if __name__ == "__main__":
    assert perform_special_sorting("Sorting1234") == "ginortS1324"
