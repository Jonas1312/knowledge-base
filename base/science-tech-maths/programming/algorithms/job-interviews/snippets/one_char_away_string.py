# Check if a string can be converted to another string with a single edit (replace char, insert char or remove char).
# O(N)


def oneaway(string1, string2):
    if len(string1) == len(string2):
        return check_replace(string1, string2)
    if len(string1) + 1 == len(string2):
        return check_insert(string1, string2)
    if len(string2) + 1 == len(string1):
        return check_insert(string2, string1)
    return False


def check_replace(string1, string2):
    edited = False
    for c1, c2 in zip(string1, string2):
        if c1 != c2:
            if edited:
                return False
            edited = True
    return True


def check_insert(small_string, long_string):
    i = j = 0
    edited = False
    while i < len(small_string) and j < len(long_string):
        if small_string[i] != long_string[j]:
            if edited:
                return False
            edited = True
            j += 1
        else:
            i += 1
            j += 1
    return True


def main():
    test_cases = [
        # no changes
        ("pale", "pale", True),
        ("", "", True),
        # one insert
        ("pale", "ple", True),
        ("ple", "pale", True),
        ("pales", "pale", True),
        ("ples", "pales", True),
        ("pale", "pkle", True),
        ("paleabc", "pleabc", True),
        ("", "d", True),
        ("d", "de", True),
        # one replace
        ("pale", "bale", True),
        ("a", "b", True),
        ("pale", "ble", False),
        # multiple replace
        ("pale", "bake", False),
        # insert and replace
        ("pale", "pse", False),
        ("pale", "pas", False),
        ("pas", "pale", False),
        ("pkle", "pable", False),
        ("pal", "palks", False),
        ("palks", "pal", False),
        # permutation with insert shouldn't match
        ("ale", "elas", False),
    ]
    for string1, string2, cmp in test_cases:
        assert oneaway(string1, string2) == cmp, f"{string1} {string2}"
    print("all good")


if __name__ == "__main__":
    main()
