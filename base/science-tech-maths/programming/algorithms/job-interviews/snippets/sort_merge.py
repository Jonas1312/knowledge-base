# time: O(nlogn)
# we have O(log n) for divide and conqueer
# and O(N) for remerging the subarrays
# space: at least O(n), with recursive implementation???
# best algorithm for sorting linked list


def mergesort(x):
    if len(x) < 2:
        return x[:]
    middle = len(x) // 2
    left_part = x[:middle]
    right_part = x[middle:]
    return merge_sorted_arrays(mergesort(left_part), mergesort(right_part))


def merge_sorted_arrays(left, right):  # left and right are already sorted, merging them
    result = [0] * (len(right) + len(left))
    i = j = k = 0  # pointers for left, right, result

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result[k] = left[i]
            i += 1
        else:
            result[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        result[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        result[k] = right[j]
        j += 1
        k += 1

    return result


def main():
    print(mergesort([1, 2, 5, 2, 3]))
    print(mergesort([1, 2, 5, 2, 3, 0]))


if __name__ == "__main__":
    main()
