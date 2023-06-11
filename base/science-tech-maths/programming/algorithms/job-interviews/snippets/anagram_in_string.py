import collections


def prime_generator():
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1


def find_anagram(string, pattern):
    assert len(string) >= len(pattern)

    prime_gen = prime_generator()
    prime_dict = collections.defaultdict(prime_gen.__next__)

    hash_pattern = hash_substring = 1
    for i, _ in enumerate(pattern):
        hash_pattern *= prime_dict[pattern[i]]
        hash_substring *= prime_dict[string[i]]

    for i in range(len(pattern), len(string) + 1):
        if hash_substring == hash_pattern:
            print(
                "Found match {} at index {}".format(
                    string[i - len(pattern) : i], i - len(pattern)
                )
            )
        if i == len(string):
            break
        hash_substring //= prime_dict[string[i - len(pattern)]]
        hash_substring *= prime_dict[string[i]]


def main():
    find_anagram(string="mdr", pattern="ùù")  # none
    find_anagram(string="mdr", pattern="mdr")  # 0
    find_anagram(string="mdr", pattern="mrd")  # 0
    find_anagram(string="BACDGABCDARVMK", pattern="ABCD")  # 0,5,6
    find_anagram(string="AAABABAA", pattern="AABA")  # 0,1,4
    find_anagram(string="mdrtmdrtmdrtlrmdolrdmcac", pattern="mdr")  # 0,4,8,13,18
    find_anagram(string="cbabadcbbabbcbabaabccbabc", pattern="abbc")  #


if __name__ == "__main__":
    main()
