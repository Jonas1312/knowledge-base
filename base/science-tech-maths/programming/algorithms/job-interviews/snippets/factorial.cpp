#include <iostream>

unsigned int factorial_rec(unsigned int n) {
    if (n < 0) {
        throw;
    }
    return n > 1 ? n * factorial_rec(n - 1) : 1;
}

unsigned int factorial_iter(unsigned int n) {
    if (n < 0) {
        throw;
    }

    unsigned int fact(1);
    for (unsigned int i = 1; i < n + 1; ++i) {
        fact *= i;
    }
    return fact;
}

int main(int argc, const char** argv) {
    std::cout << factorial_rec(0) << std::endl;
    std::cout << factorial_rec(1) << std::endl;
    std::cout << factorial_rec(4) << std::endl;   // 2 3 4
    std::cout << factorial_rec(10) << std::endl;  // 3628800
    std::cout << factorial_iter(0) << std::endl;
    std::cout << factorial_iter(1) << std::endl;
    std::cout << factorial_iter(4) << std::endl;   // 2 3 4
    std::cout << factorial_iter(10) << std::endl;  // 3628800
    return 0;
}
