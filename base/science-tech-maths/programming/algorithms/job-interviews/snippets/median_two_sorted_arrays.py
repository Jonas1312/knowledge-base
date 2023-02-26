# https://www.byte-by-byte.com/median/


def median_array(array):
    len_ = len(array)
    if len_ % 2 != 0:
        median = array[len_ // 2]
    else:
        median = (array[len_ // 2 - 1] + array[len_ // 2]) / 2
    return median


def median_sorted_arrays(A, B):
    # Recursively find the median. We remove ~half the items from above and
    # below the median on each turn, resulting in O(n log n) runtime
    assert len(A) == len(B)

    median_a = median_array(A)
    median_b = median_array(B)

    if median_a == median_b:
        return median_a

    if len(A) <= 2:
        return median_array(sorted(A + B))

    # A always biggest median
    if median_b > median_a:
        A, B = B, A

    print("before: ", A, B)
    odd_len = len(A) % 2 != 0
    # we drop the second highest part of A, since it doesn't contain the median
    index_split_a = len(A) // 2 + 1
    A = A[:index_split_a]
    index_split_b = len(B) // 2 if odd_len else len(B) // 2 - 1
    B = B[index_split_b:]
    print("after: ", A, B)

    return median_sorted_arrays(A, B)


def main():
    # print(median_array([1, 3, 5]))
    # print(median_array([1, 2, 3, 4, 5, 6]))
    print(median_sorted_arrays([3, 5], [2, 4]))  # 3.5
    print(median_sorted_arrays([2, 4, 6], [1, 3, 5]))  # 3.5
    print(median_sorted_arrays([1, 2, 3, 4, 5, 6], [0, 0, 0, 0, 10, 10]))  # 2.5


if __name__ == "__main__":
    main()
