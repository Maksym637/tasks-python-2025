#
# Time complexity:
# > Average case: O(nlog(n))
# > Worst case: O(n^2)
#
def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[len(array) // 2]

    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
    input_array = [9, 7, 5, 11, 12, 2, 14, 3, 10, 6]
    output_array = [2, 3, 5, 6, 7, 9, 10, 11, 12, 14]

    assert quick_sort(input_array) == output_array
