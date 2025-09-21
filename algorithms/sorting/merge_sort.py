#
# Time complexity:
# > Average case: O(nlog(n))
# > Worst case: O(nlog(n))
#
def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2

    left_half = merge_sort(lst[:mid])
    right_half = merge_sort(lst[mid:])

    return merge(left_half, right_half)


def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


if __name__ == "__main__":
    input_array = [9, 7, 5, 11, 12, 2, 14, 3, 10, 6]
    output_array = [2, 3, 5, 6, 7, 9, 10, 11, 12, 14]

    assert merge_sort(input_array) == output_array
