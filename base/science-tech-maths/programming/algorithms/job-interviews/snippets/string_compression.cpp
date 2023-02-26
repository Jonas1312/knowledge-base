#include <iostream>
#include <vector>

int compute_compressed_length(const std::string &input_string) {
    if (input_string.size() <= 0) {
        return 0;
    }
    if (input_string.size() == 1) {
        return 2;
    }

    int compressed_length = 0;
    int consecutive = 1;
    for (int i = 0; i < input_string.size(); ++i) {
        if (i + 1 >= input_string.length()) {
            compressed_length += std::to_string(consecutive).size() + 1;  // 1 for the letter
        } else if (input_string[i] != input_string[i + 1]) {
            compressed_length += std::to_string(consecutive).size() + 1;  // 1 for the letter
            consecutive = 1;                                              // reset counter
        } else {
            consecutive += 1;
        }
    }
    return compressed_length;
}

std::string string_compress(const std::string &input_string) {
    int compressed_length = compute_compressed_length(input_string);

    if (compressed_length >= input_string.length()) {
        return input_string;
    }

    std::string compressed_string(compressed_length, '_');

    int consecutive = 1;
    int j = 0;
    for (int i = 0; i < input_string.size(); ++i) {
        if (i + 1 >= input_string.length()) {
            std::string encoding(input_string[i] + std::to_string(consecutive));  // char + str(count)
            compressed_string.replace(j, encoding.size(), encoding);
            // j += encoding.size();
            // consecutive = 1;  // reset counter
        } else if (input_string[i] != input_string[i + 1]) {
            std::string encoding(input_string[i] + std::to_string(consecutive));  // char + str(count)
            compressed_string.replace(j, encoding.size(), encoding);
            j += encoding.size();
            consecutive = 1;  // reset counter
        } else {
            consecutive += 1;
        }
    }

    return compressed_string;
}

int main() {
    std::cout << (compute_compressed_length("aabcccccaaa") == 8) << std::endl;
    std::cout << (compute_compressed_length("abcdef") == 12) << std::endl;
    std::cout << (compute_compressed_length("aabb") == 4) << std::endl;
    std::cout << (compute_compressed_length("aaa") == 2) << std::endl;
    std::cout << (compute_compressed_length("a") == 2) << std::endl;
    std::cout << (compute_compressed_length("") == 0) << std::endl;

    std::cout << string_compress("aabcccccaaa").compare("a2b1c5a3") << std::endl;
    std::cout << string_compress("abcdef").compare("abcdef") << std::endl;
    std::cout << string_compress("aabb").compare("aabb") << std::endl;
    std::cout << string_compress("aaa").compare("a3") << std::endl;
    std::cout << string_compress("a").compare("a") << std::endl;
    std::cout << string_compress("").compare("") << std::endl;
}
