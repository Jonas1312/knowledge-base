# when given an array of length n + 1 containing integers 1 through n, find the duplicate integer in an array.
# sum(1 to n) = n(n + 1) / 2
# If I used the formula to calculate the expected sum, then summed all the integers in the array
# the difference between the two values would be the duplicate number. Cool!


def find_dup(x):
    n = len(x) - 1
    sum_formula = n * (n + 1) // 2
    diff = sum(x) - sum_formula
    return diff


if __name__ == "__main__":
    print(find_dup([1, 2, 3, 3, 4]) == 3)
    print(find_dup([1, 2, 3, 2, 4]) == 2)
    print(find_dup([1, 2, 3, 1, 4]) == 1)
