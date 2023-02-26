// circular array to store the K last lines of a file
#include <fstream>
#include <iostream>
#include <vector>

void print_last_k_lines(const std::string& filename, int K) {
    std::ifstream myfile(filename);
    std::vector<std::string> last_k_lines;
    last_k_lines.reserve(K);

    if (myfile.is_open()) {
        int start(0);

        std::string buffer;
        while (std::getline(myfile, buffer)) {
            if (last_k_lines.size() < K) {
                last_k_lines.push_back(buffer);
            } else {
                last_k_lines[start++] = buffer;
                start = start % K;
            }
        }

        myfile.close();

        // print nodes
        for (int i = 0; i < last_k_lines.size(); ++i) {
            std::cout << last_k_lines[(start + i) % K] << std::endl;
        }

    }

    else {
        std::cout << "Unable to open file";
    }
}

int main(int argc, const char** argv) {
    print_last_k_lines("print_last_K_lines.cpp", 10);
    return 0;
}
