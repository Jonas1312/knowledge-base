#include <iostream>
#include <vector>

// recursive with pointers
int* binary_search_pointers(int* begin, int* end, int value) {
    if (!(begin <= end)) {
        return nullptr;
    }
    int* middle = begin + (end - begin) / 2;

    if (*middle > value) {
        return binary_search_pointers(begin, middle - 1, value);
    } else if (*middle < value) {
        return binary_search_pointers(middle + 1, end, value);
    } else {
        return middle;
    }
}

int binary_search_vector(const std::vector<int>& input_vec, int value) {
    if (input_vec.size() == 0) {
        return -1;
    }

    int begin(0);
    int end(input_vec.size() - 1);

    int middle;

    while (begin <= end) {
        middle = begin + (end - begin) / 2;
        if (input_vec[middle] > value) {
            end = middle - 1;
        } else if (input_vec[middle] < value) {
            begin = middle + 1;
        } else {
            return middle;
        }
    }
    return -1;
}

int main(int argc, const char** argv) {
    int my_array_normal[]{1, 2, 3, 4, 5, 6, 7};
    std::cout << (*binary_search_pointers(&(my_array_normal[0]), &(my_array_normal[6]), 4) == 4) << std::endl;
    std::cout << (*binary_search_pointers(&(my_array_normal[0]), &(my_array_normal[6]), 7) == 7) << std::endl;
    std::cout << (*binary_search_pointers(&(my_array_normal[0]), &(my_array_normal[6]), 2) == 2) << std::endl;
    std::cout << (*binary_search_pointers(&(my_array_normal[0]), &(my_array_normal[5]), 5) == 5) << std::endl;
    std::cout << (binary_search_pointers(&(my_array_normal[0]), &(my_array_normal[5]), 42) == nullptr) << std::endl;
    int my_array_empty[]{};
    std::cout << (binary_search_pointers(&(my_array_empty[0]), &(my_array_empty[0]), 5) == nullptr) << std::endl;
    int my_array_unique[]{1};
    std::cout << (*binary_search_pointers(&(my_array_unique[0]), &(my_array_unique[0]), 1) == 1) << std::endl;

    std::vector<int> my_vec{1, 2, 3, 4, 5, 6, 7};
    std::cout << (my_vec.at(binary_search_vector(my_vec, 4)) == 4) << std::endl;
    std::cout << (my_vec.at(binary_search_vector(my_vec, 7)) == 7) << std::endl;
    std::cout << (my_vec.at(binary_search_vector(my_vec, 1)) == 1) << std::endl;
    my_vec = {1, 2, 3, 4, 5, 6};
    std::cout << (my_vec.at(binary_search_vector(my_vec, 1)) == 1) << std::endl;
    std::cout << (my_vec.at(binary_search_vector(my_vec, 6)) == 6) << std::endl;
    std::cout << (my_vec.at(binary_search_vector(my_vec, 3)) == 3) << std::endl;
    std::cout << (my_vec.at(binary_search_vector(my_vec, 4)) == 4) << std::endl;
    std::cout << (binary_search_vector(my_vec, 42) == -1) << std::endl;
    my_vec = {1};
    std::cout << (my_vec.at(binary_search_vector(my_vec, 1)) == 1) << std::endl;
    my_vec.clear();
    std::cout << (binary_search_vector(my_vec, 1) == -1) << std::endl;

    return 0;
}
