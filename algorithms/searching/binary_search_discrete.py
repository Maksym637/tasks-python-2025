def binary_search_iterative(data, target):
    low = 0
    high = len(data)

    while high - low > 1:
        mid = (low + high) // 2

        if target < data[mid]:
            high = mid
        else:
            low = mid

    return low if data[low] == target else None


def binary_search_recursive(data, target, low, high):
    if high - low <= 1:
        return low if data[low] == target else None

    mid = (low + high) // 2

    if target < data[mid]:
        return binary_search_recursive(data, target, low, mid)
    else:
        return binary_search_recursive(data, target, mid, high)


if __name__ == "__main__":
    print(binary_search_iterative([1, 2, 3, 4, 5, 6], 4))
    print(binary_search_recursive([1, 2, 3, 4, 5, 6], 4))
