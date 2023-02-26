#include <iostream>
#include <string>

void fizzbuzz_1(int n) {
    bool fizz, buzz;
    for (int i = 1; i <= n; ++i) {
        fizz = !static_cast<bool>(i % 3);
        buzz = !static_cast<bool>(i % 5);

        if (fizz && buzz)  // 15 must be tested first !!!
            std::cout << "FizzBuzz, ";
        else if (buzz)
            std::cout << "Buzz, ";
        else if (fizz)
            std::cout << "Fizz, ";
        else
            std::cout << i << ", ";
    }
}

// modulo operation is O(N²)
void fizzbuzz_2(int n) {
    std::string d;
    for (int i = 1; i <= n; i++) {
        d = "";
        if (i % 3 == 0) d += "Fizz";
        if (i % 5 == 0) d += "Buzz";
        if (d == "")
            std::cout << i << ", ";
        else
            std::cout << d << ", ";
    }
}

int main() {
    fizzbuzz_1(10);
    std::cout << std::endl;
    fizzbuzz_2(10);

    return EXIT_SUCCESS;
}
