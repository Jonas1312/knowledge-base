#include <iostream>
#include <vector>

template <typename T>
void print_vec(const std::vector<T> &vec) {
    for (const auto &x : vec) {
        std::cout << x << ", ";
    }
    std::cout << std::endl;
}

template <typename T>
void merge_two_sorted_arrays(std::vector<T> &vec, int begin_left, int end_left, int begin_right, int end_right) {
    std::vector<T> temp_vec(end_right - begin_left + 1);

    int i = begin_left;
    int j = begin_right;
    int k = 0;

    while ((i <= end_left) && (j <= end_right)) {
        if (vec[i] < vec[j]) {
            temp_vec[k++] = vec[i++];
        } else {
            temp_vec[k++] = vec[j++];
        }
    }

    while (i <= end_left) {
        temp_vec[k++] = vec[i++];
    }

    while (j <= end_right) {
        temp_vec[k++] = vec[j++];
    }

    // copy temp_vec back to original array
    for (int i = begin_left, k = 0; i <= end_right;) {
        vec[i++] = temp_vec[k++];
    }
}

template <typename T>
void mergesort(std::vector<T> &vec, int begin, int end) {
    auto size = end - begin + 1;

    // array with a single value
    if (size < 2) {
        return;
    }

    int middle = begin + size / 2;  // since size >= 2, we know middle > begin

    mergesort(vec, begin, middle - 1);
    mergesort(vec, middle, end);
    merge_two_sorted_arrays(vec, begin, middle - 1, middle, end);
}

template <typename T>
void mergesort(std::vector<T> &vec) {
    mergesort(vec, 0, vec.size() - 1);
}

int main(int argc, char const *argv[]) {
    std::vector<int> my_vec{1, 2, 5, 2, 3};

    mergesort(my_vec);
    print_vec(my_vec);

    my_vec = {1, 2, 5, 2, 3, 0};
    mergesort(my_vec);
    print_vec(my_vec);

    return 0;
}
