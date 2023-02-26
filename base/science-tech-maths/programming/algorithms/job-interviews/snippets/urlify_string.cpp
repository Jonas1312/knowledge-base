#include <iostream>
#include <string>
#include <vector>

std::string urlify(std::string input_string, int true_length) {
    int late_index = input_string.size() -1;

    for (int i = true_length - 1; i >= 0; --i) {
        if (input_string[i] == ' ') {
            input_string.at(late_index--) = '%';
            input_string.at(late_index--) = '2';
            input_string.at(late_index--) = '0';
        } else {
            input_string.at(late_index--) = input_string.at(i);
        }
    }
    return input_string;
}

int main() {
    std::cout << urlify("much ado about nothing      ", 22).compare("much%20ado%20about%20nothing") << std::endl;
    std::cout << urlify("Mr John Smith    ", 13).compare("Mr%20John%20Smith") << std::endl;
    std::cout << urlify(" a b       ", 5).compare("%20a%20b%20") << std::endl;
    std::cout << urlify(" a b    ", 4).compare("%20a%20b") << std::endl;
    return 0;
}
