from collections import defaultdict


def find_pattern_in_substring(input_string, pattern):
    assert len(input_string) >= len(pattern)

    dic_pattern = defaultdict(lambda: 0)
    dic_string = defaultdict(lambda: 0)
    for x in pattern:  # count nb of occurrences for each character
        dic_pattern[x] += 1

    r_pointer = l_pointer = 0
    best_l_pointer, best_r_pointer = 0, len(input_string)

    matches = 0
    for i, x in enumerate(input_string):
        dic_string[x] += 1

        if dic_pattern[x] != 0 and dic_string[x] <= dic_pattern[x]:
            matches += 1

        if matches == len(pattern):
            r_pointer = i
            while (
                dic_string[input_string[l_pointer]] > dic_pattern[input_string[l_pointer]]
                or dic_pattern[input_string[l_pointer]] == 0
            ):
                if dic_string[input_string[l_pointer]] > dic_pattern[input_string[l_pointer]]:
                    dic_string[input_string[l_pointer]] -= 1
                l_pointer += 1

            if best_r_pointer - best_l_pointer > r_pointer - l_pointer:
                best_l_pointer = l_pointer
                best_r_pointer = r_pointer
    if matches == len(pattern):
        return input_string[best_l_pointer : best_r_pointer + 1]
    return None


def main():
    print(find_pattern_in_substring("motorolaestletelephone", "roest"))
    print(find_pattern_in_substring("mdrjfk", "df"))
    print(find_pattern_in_substring("mdrjfkdf", "df"))
    print(find_pattern_in_substring("ffffffffffffabvcde", "fab"))
    print(find_pattern_in_substring("ddddd", "fab"))
    print(find_pattern_in_substring("fab", "fab"))


if __name__ == "__main__":
    main()
