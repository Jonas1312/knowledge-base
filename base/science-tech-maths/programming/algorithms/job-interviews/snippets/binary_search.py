def binary_search_recurs(array, value, begin=None, end=None):
    if begin is None:
        begin = 0
    if end is None:
        end = len(array) - 1

    if not begin <= end:
        return -1

    middle = (end + begin) // 2
    if array[middle] > value:
        return binary_search_recurs(array, value, begin, middle - 1)
    elif array[middle] < value:
        return binary_search_recurs(array, value, middle + 1, end)
    else:
        return middle


def binary_search_iter(array, value):
    if len(array) == 0:
        return -1

    begin = 0
    end = len(array) - 1  # important!!!

    while begin <= end:
        middle = (end + begin) // 2
        if array[middle] > value:
            end = middle - 1
        elif array[middle] < value:
            begin = middle + 1
        else:
            return middle
    return -1


def main():
    print(binary_search_iter([1, 2, 3, 4, 5, 6, 7], value=1) == 0)
    print(binary_search_iter([1, 2, 3, 4, 5, 6, 7], value=7) == 6)
    print(binary_search_iter([1, 2, 3, 4, 5, 6, 7], value=4) == 3)
    print(binary_search_iter([1, 2, 3, 4, 5, 6, 7], value=42) == -1)
    print(binary_search_iter([1, 2, 3, 4, 5, 6], value=1) == 0)
    print(binary_search_iter([1, 2, 3, 4, 5, 6], value=6) == 5)
    print(binary_search_iter([1, 2, 3, 4, 5, 6], value=4) == 3)
    print(binary_search_iter([1, 2, 3, 4, 5, 6], value=3) == 2)
    print(binary_search_iter([1, 2, 3, 4, 5, 6], value=42) == -1)
    print(binary_search_iter([1], value=1) == 0)
    print(binary_search_iter([1], value=42) == -1)
    print(binary_search_iter([], value=42) == -1)
    print("recurs", "-" * 42)
    print(binary_search_recurs([1, 2, 3, 4, 5, 6, 7], value=1) == 0)
    print(binary_search_recurs([1, 2, 3, 4, 5, 6, 7], value=7) == 6)
    print(binary_search_recurs([1, 2, 3, 4, 5, 6, 7], value=4) == 3)
    print(binary_search_recurs([1, 2, 3, 4, 5, 6, 7], value=42) == -1)
    print(binary_search_recurs([1, 2, 3, 4, 5, 6], value=1) == 0)
    print(binary_search_recurs([1, 2, 3, 4, 5, 6], value=6) == 5)
    print(binary_search_recurs([1, 2, 3, 4, 5, 6], value=4) == 3)
    print(binary_search_recurs([1, 2, 3, 4, 5, 6], value=3) == 2)
    print(binary_search_recurs([1, 2, 3, 4, 5, 6], value=42) == -1)
    print(binary_search_recurs([1], value=1) == 0)
    print(binary_search_recurs([1], value=42) == -1)
    print(binary_search_recurs([], value=42) == -1)


if __name__ == "__main__":
    main()
