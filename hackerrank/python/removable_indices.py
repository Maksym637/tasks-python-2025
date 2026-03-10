#
# Problem description:
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#   1. STRING str1
#   2. STRING str2
#
# Example:
# Input:
# str1 = aabbb
# str2 = aabb
# Output:
# 2, 3, 4
#
def getRemovableIndices(str1: str, str2: str) -> list[int]:
    indices = []

    for i in range(len(str1)):
        new_str1 = str1[:i] + str1[i + 1 :]
        if new_str1 == str2:
            indices.append(i)

    if not indices:
        return [-1]

    return indices


if __name__ == "__main__":
    assert getRemovableIndices("aabbb", "aabb") == [2, 3, 4]
    assert getRemovableIndices("abc", "abc") == [-1]
