# N: array size
# K: integer range (max - min)
# time: O(N+K)
# space: O(K)

# we know the integer range. we can use a "counting" array.
def countingsort(x):
    max_value = max(x)
    min_value = min(x)
    print("min, max: ", min_value, max_value)

    count_array = [0] * (max_value - min_value + 1)
    print("len: ", len(count_array))

    for value in x:
        # print(value, min_value)
        count_array[value - min_value] += 1

    index_input_array = 0
    for index, nb_occurences in enumerate(count_array):
        for _ in range(nb_occurences):
            x[index_input_array] = index + min_value
            index_input_array += 1

    return x


def main():
    print(countingsort([1, 2, 5, 2, 3]))
    print(countingsort([1, 2, 5, 2, 3, 0]))


if __name__ == "__main__":
    main()
