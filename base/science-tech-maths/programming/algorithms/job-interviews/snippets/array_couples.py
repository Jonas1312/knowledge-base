"""
Given an array of positive integers, array of even size.
We want to know if each pair of integers, [k, k+1], [k+2, k+3], [k+4, k+5], ...,
appears in the reverse order in the array.

If yes, return the string "yes".
Otherwise, return a string of integers separated by commas, representing the pair that has no reverse in the array.
"""


def array_couples(arr: list[int]):
    backward_pairs = {}
    alone_pairs = []

    # we start by iterating over the backward pairs, and store them in hashmap, with their position in the array
    # this take O(n) in time
    for i, (first, second) in enumerate(zip(arr[0::2], arr[1::2])):
        backward_pairs[f"{second},{first}"] = i

    # then, we iterate over the forward pairs, and check if they are in the hashmap, at diff position
    # this takes O(n) in time
    for i, (first, second) in enumerate(zip(arr[0::2], arr[1::2])):
        forward_pair = f"{first},{second}"

        if forward_pair in backward_pairs and i != backward_pairs[forward_pair]:
            continue

        alone_pairs.append(forward_pair)

    if alone_pairs:
        return ",".join(alone_pairs)

    return "yes"


def main():
    assert array_couples([2, 1, 1, 2, 3, 3]) == "3,3"
    assert array_couples([5, 4, 6, 7, 7, 6, 4, 5]) == "yes"
    assert array_couples([4, 5, 1, 4, 5, 4, 4, 1]) == "yes"
    assert array_couples([6, 2, 2, 6, 5, 14, 14, 1]) == "5,14,14,1"
    assert array_couples([1, 2, 3, 4, 5, 6, 6, 5, 4, 3, 2, 10]) == "1,2,2,10"
    assert array_couples([1, 2, 2, 4]) == "1,2,2,4"


if __name__ == "__main__":
    main()
