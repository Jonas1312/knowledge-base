#include <iostream>
#include <unordered_map>
#include <vector>

void algo_1(const std::vector<int> input_array, const int K) {
    int sum = 0;
    size_t begin = 0;
    size_t end = 0;

    while (true) {
        if (sum == K) {
            for (auto i = begin; i < end; ++i) {
                std::cout << input_array[i] << ", ";
            }
            std::cout << std::endl;

            sum -= input_array.at(begin);
            begin++;
        } else if (sum < K) {
            if (end == input_array.size()) {
                break;
            }
            sum += input_array.at(end);
            end++;
        } else if (sum > K) {
            sum -= input_array.at(begin);
            begin++;
        }
    }
}

void algo_2(const std::vector<int> input_array, const int K) {
    std::unordered_map<int, int> sums_hashmap;
    int sum = 0;

    for (size_t i = 0; i < input_array.size(); ++i) {
        sum += input_array.at(i);
        sums_hashmap[sum] = i;

        if (sums_hashmap.contains(sum - K)) {
            size_t begin = sums_hashmap[sum - K] + 1;
            size_t end = i + 1;
            for (size_t j = begin; j < end; ++j) {
                std::cout << input_array[j] << ", ";
            }
            std::cout << std::endl;
        }
    }
}

int main(int argc, char const *argv[]) {
    algo_1({2, 6, 0, 9, 7, 3, 1, 4, 1, 10}, 15);  // {6, 0, 9}, {7, 3, 1, 4}, {4, 1, 10}
    std::cout << "--------------------------------" << std::endl;
    algo_2({2, 6, 0, 9, 7, 3, 1, 4, 1, 10}, 15);  // {6, 0, 9}, {7, 3, 1, 4}, {4, 1, 10}
    std::cout << "--------------------------------" << std::endl;
    algo_2({0, 5, -7, 1, -4, 7, 6, 1, 4, 1, 10}, 15);  // {1, -4, 7, 6, 1, 4} or {4, 1, 10}
    std::cout << "--------------------------------" << std::endl;
    algo_2({0, 5, -7, 1, -4, 7, 6, 1, 4, 1, 10}, -3);  // {1, -4}
    return 0;
}
