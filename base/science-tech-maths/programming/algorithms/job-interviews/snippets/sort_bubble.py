# time: O(N²)
# best: O(N), cause just one pass if already sorted
# space: O(1)


def bubblesort(x):
    n = len(x)

    for i in range(n):
        for j in range(0, n - 1 - i):  # "-i" because last element(s) already sorted. "-1" because x[j+1] out of bounds.
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]
    return x


def main():
    print(bubblesort([1, 2, 5, 2, 3]))
    print(bubblesort([1, 2, 5, 2, 3, 0]))


if __name__ == "__main__":
    main()
