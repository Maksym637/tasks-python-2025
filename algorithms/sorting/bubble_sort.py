#
# Time complexity:
# > Average case: O(n^2)
# > Worst case: O(n^2)
#
def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


if __name__ == "__main__":
    input_array = [9, 7, 5, 11, 12, 2, 14, 3, 10, 6]
    output_array = [2, 3, 5, 6, 7, 9, 10, 11, 12, 14]

    assert bubble_sort(input_array) == output_array
