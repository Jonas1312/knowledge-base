# we replace spaces in a backward way so that we can do it inplace
def urlify_complex(string, true_length):
    char_list = list(string)  # python string are immutable

    end_pointer = len(string)

    for i in reversed(range(true_length)):
        if string[i] == " ":  # space in between words
            char_list[end_pointer - 3 : end_pointer] = r"%20"
            end_pointer -= 3
        else:  # real character
            char_list[end_pointer - 1] = string[i]
            end_pointer -= 1

    ret = "".join(char_list)
    print(ret)
    return ret


def urlify_pythonic(string, true_length):
    return string[:true_length].replace(" ", "%20")


def main():
    urlify = urlify_pythonic
    assert urlify("much ado about nothing      ", 22) == r"much%20ado%20about%20nothing"
    assert urlify("Mr John Smith    ", 13) == r"Mr%20John%20Smith"
    assert urlify(" a b       ", 5) == r"%20a%20b%20"
    assert urlify(" a b    ", 4) == r"%20a%20b"


if __name__ == "__main__":
    main()
