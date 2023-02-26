#include <algorithm>
#include <iostream>
#include <vector>

bool are_permutation_sort(std::string str1, std::string str2) {
    if (str1.size() != str2.size()) {
        return false;
    }

    std::sort(str1.begin(), str1.end());
    std::sort(str2.begin(), str2.end());

    for (int i = 0; i < str1.size(); ++i) {
        if (str1.at(i) != str2.at(i)) {
            return false;
        }
    }
    return true;
}

bool are_permutation_count(std::string str1, std::string str2) {
    if (str1.size() != str2.size()) {
        return false;
    }

    std::vector<int> char_count(256);

    for (const char &character : str1) {
        char_count[character] += 1;
    }

    for (const char &character : str2) {
        char_count[character] -= 1;
        if (char_count[character] < 0) {
            return false;
        }
    }
    return true;
}

int main() {
    std::cout << are_permutation_sort("testest", "estxest") << std::endl;
    std::cout << are_permutation_count("testest", "estxest") << std::endl;
    std::cout << are_permutation_sort("hello", "oellh") << std::endl;
    std::cout << are_permutation_count("hello", "oellh") << std::endl;

    return 0;
}
