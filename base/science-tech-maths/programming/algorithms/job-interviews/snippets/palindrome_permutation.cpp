#include <bitset>
#include <iostream>

bool is_palindrome(std::string input_string) {
    std::bitset<256> char_vector;
    int num_valid_chars = 0;

    for (const char &c : input_string) {
        if ((c >= 65 && c <= 90) || (c >= 97 && c <= 122)) {
            char_vector.flip(c);
            num_valid_chars++;
        }
    }
    // even nb of chars and all even count
    if (num_valid_chars % 2 == 0 && char_vector.none()) {
        return true;
    }
    // odd nb of chars and just one with an odd count
    else if (num_valid_chars % 2 == 1 && char_vector.count() == 1) {
        return true;
    }

    return false;
}

int main() {
    std::cout << (is_palindrome("aba") == true) << std::endl;
    std::cout << (is_palindrome("aab") == true) << std::endl;
    std::cout << (is_palindrome("abba") == true) << std::endl;
    std::cout << (is_palindrome("aabb") == true) << std::endl;
    std::cout << (is_palindrome("a-bba") == true) << std::endl;
    std::cout << (is_palindrome("a-bba!") == true) << std::endl;
    std::cout << (is_palindrome("tact coa") == true) << std::endl;
    std::cout << (is_palindrome("jhsabckuj ahjsbckj") == true) << std::endl;
    std::cout << (is_palindrome("able was i ere i saw elba") == true) << std::endl;
    std::cout << (is_palindrome("so patient a nurse to nurse a patient so") == false) << std::endl;
    std::cout << (is_palindrome("random words") == false) << std::endl;
    std::cout << (is_palindrome("not a palindrome") == false) << std::endl;
    std::cout << (is_palindrome("no x in nixon") == true) << std::endl;
    std::cout << (is_palindrome("azaz") == true) << std::endl;
    return 0;
}
