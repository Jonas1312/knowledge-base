// check if string has all unique characters

#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

// linear but not O(1) in space
bool is_unique_charset(const std::string &input_string) {
    std::vector<bool> charset(256, false);
    for (const char &character : input_string) {
        if (charset[character]) {
            return false;
        }
        charset.at(character) = true;
    }

    return true;
}

// sort in place, can't be const anymore and we use a copy
bool is_unique_sort(std::string input_string) {
    std::sort(input_string.begin(), input_string.end());
    for (int i = 0; i < input_string.size() - 1; ++i) {
        if (input_string.at(i) == input_string.at(i + 1)) {
            return false;
        }
    }
    return true;
}

int main() {
    std::vector<std::string> words = {"abcde", "hello", "apple", "kite", "padle"};

    for (const auto &word : words) {
        std::cout << word << ": " << is_unique_charset(word) << std::endl;
        std::cout << word << ": " << is_unique_sort(word) << std::endl;
    }

    return 0;
}
