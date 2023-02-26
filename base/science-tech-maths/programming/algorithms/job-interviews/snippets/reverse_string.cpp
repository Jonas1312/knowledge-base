#include <iostream>

void reverse(char *start) {  // copy of the pointer
    char *end = start;
    while (*end) {  // the last character of the char array is '\0' == NULL == 0x00. The number '0' == 0x30 !!!
        end++;      // we move the end pointer until the end
    }
    --end;  // we don't touch the last char '\0'

    // swap characters
    while (start < end) {  // compare addresses
        std::swap(*start++, *end--);
    }
}

int main(int argc, char const *argv[]) {
    char my_string[] = "reverse me plz";  // { 'r', ..., 'z', '\0' }
    std::cout << my_string << std::endl;
    reverse(my_string);
    std::cout << my_string
              << std::endl;  // my_string pointer is still at the same position, since reverse() used a copy
    return 0;
}
