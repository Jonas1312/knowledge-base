"""
You are given a string (s) of letters.
You must find the length of the longest substring without character repetition.
PS: You should consider lower case letters different from upper case letters.
"""


def longest_sub(s):
    dic = {}
    l_pointer = i = 0
    best_length = 0
    while i < len(s):
        if s[i] in dic:  # character already known
            l_pointer = dic[s[i]] + 1  # move l_pointer to last know position + 1
        dic[s[i]] = i  # update last known position of this char
        i += 1
        if i - l_pointer > best_length:
            best_length = i - l_pointer
    return best_length


def main():
    print(longest_sub("abcAbCds"))  # 6, cAbCds
    print(longest_sub("ABDEFGABEF"))  # 6
    print(longest_sub("abcabcaasddd"))  # 3
    print(longest_sub("wintics"))  # 5
    print(longest_sub("WintICsAI"))  # 8


if __name__ == "__main__":
    main()
