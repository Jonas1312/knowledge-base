def permutations_1(input_string, left=None, right=None):
    if isinstance(input_string, str):
        input_string = list(input_string)
    if (left or right) is None:
        left, right = 0, len(input_string)
    if left == right:
        print("".join(input_string))
    else:
        for i in range(left, right):
            input_string[i], input_string[left] = input_string[left], input_string[i]
            permutations_1(input_string, left=left + 1, right=right)  # type: ignore
            input_string[i], input_string[left] = input_string[left], input_string[i]


# we insert the "prefix" in at every possible point in string
# n! calls when prefix is full, it's just string permutation
# but there's also calls when input_string is not empty
# we have a tree with !n leaves
# each leave as a path of length n
# so we have at most O(n*n!) calls
# each call is O(N) (print, concatenation)
# TOTAL RUNTIME: O(N²N!)
def permutations_2(input_string, prefix=None):
    if isinstance(input_string, str):
        input_string = list(input_string)
    prefix = prefix or []
    if len(input_string) == 0:
        print("".join(prefix))  # takes O(N) to print
    else:
        for i, _ in enumerate(input_string):
            rem = input_string[:i] + input_string[i + 1 :]  # O(N) for concatenation
            permutations_2(rem, prefix + [input_string[i]])


def main():
    permutations_2("abcd")  # n! prints for a string of size n


if __name__ == "__main__":
    main()
