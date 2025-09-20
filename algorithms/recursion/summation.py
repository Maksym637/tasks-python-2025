def sum_array(array, index=0):
    if index == len(array):
        return 0

    return array[index] + sum_array(array, index + 1)


if __name__ == "__main__":
    print(sum_array([1, 2, 3, 4, 5]))
