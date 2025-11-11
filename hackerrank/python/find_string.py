# Problem description: https://www.hackerrank.com/challenges/find-a-string/problem
def count_substring(string: str, sub_string: str) -> int:
    counter = 0
    len_sub_string = len(sub_string)

    for i in range(len(string)):
        if string[i : len_sub_string + i] == sub_string:
            counter += 1

    return counter


if __name__ == "__main__":
    assert count_substring("ABCDCDC", "CDC") == 2
