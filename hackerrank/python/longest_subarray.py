#
# Problem description:
# Find the longest contiguous subarray
# Input:
# [1, 2, 4, 3, 2, 2]
# Output:
# [3, 2, 2] = 3
#
def get_longest_subarray(arr: list[int]) -> int:
    k = 0
    count, max_count = 0, 0

    for i in range(len(arr)):
        left = k
        right = i + 1

        if right > left:
            if (max(arr[left:right]) - min(arr[left:right])) <= 1:
                count = right - left
            else:
                k += 1

        if count > max_count:
            max_count = count

    return max_count


if __name__ == "__main__":
    tests = [
        ([1, 1, 1, 3, 3, 2, 2], 4),
        ([1, 1, 1, 1, 1, 1, 1], 7),
        ([1, 2, 3, 4, 5, 6, 7], 2),
        ([1, 2, 2, 1, 2], 5),
        ([1, 2, 2, 3, 1, 2], 3),
        ([1, 2, 1, 3, 4], 3),
        ([1, 2, 3, 3, 2, 2], 5),
        ([1, 4, 2, 3, 3, 2, 2], 5),
        ([1, 5, 2, 2, 3, 2, 2], 5),
        ([4, 1, 2, 2, 3, 3, 2], 5),
        ([], 0),
        ([100, 10, 100, 10, 100, 10], 1),
        ([1, 2, 4, 3, 2, 2], 3),
    ]

    for test_data, expected in tests:
        assert get_longest_subarray(test_data) == expected
