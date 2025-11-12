# Problem description: https://www.hackerrank.com/challenges/python-mutations/problem
def mutate_string(string: str, position: int, character: str) -> str:
    list_string = list(string)
    list_string[position] = character
    return "".join(list_string)


if __name__ == "__main__":
    assert mutate_string("abracadabra", 5, "k") == "abrackdabra"
