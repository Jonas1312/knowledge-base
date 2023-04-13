"""
Write a function that given a string, determines if it is a concatenation of 2 dictionary words.
"""


def solution_1(input_string: str, dictionnary):
    """Naive solution.

    Space is O(1) since left_part and right_part are views of the input string.

    Time complexity:

    - N is the length of the input string.
    - Two parts of length i and N-i are checked in the dictionnary.
    - Computing the hash of the string is O(N), lookup in dict is O(1).
    - There are N dict lookups, so the time complexity is O(N^2).

    """
    for i in range(1, len(input_string)):
        left_part, right_part = input_string[:i], input_string[i:]
        if left_part in dictionnary and right_part in dictionnary:
            return True


def solution_2(input_string: str, dictionnary):
    """Faster dict lookup

    We can use a trie to check if a string is in the data structure.

    Checking the left_part of string would take O(N) time.

    Checking the right_part is more difficult. We need to store the dictionary words in reverse order in a trie.

    It would take O(N) time to check if the right_part is in the trie.

    The total algorithm is 0(N).
    """


"""
Write a function that given a string, determines if it is a concatenation of K dictionary words.

K can be 1 or more.
"""


def solution_3(input_string: str, dictionnary):
    """Naive recursive solution.

    One can add some cache
    """
    if input_string in dictionnary:
        return True

    for i in range(1, len(input_string)):
        left_part, right_part = input_string[:i], input_string[i:]
        if left_part in dictionnary and solution_3(right_part, dictionnary):
            return True
