#include <fstream>
#include <iostream>
#include <algorithm>
#include <string>

int calNum(std::string line) {
    int first = int(line[line.find_first_of("0123456789")] - '0');
    reverse(line.begin(), line.end());
    int last = int(line[line.find_first_of("0123456789")] - '0');
    return first*10 + last;
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cout << "Improper arguments, expects file name" << std::endl;
        return EXIT_FAILURE;
    }

    std::ifstream input;
    input.open(argv[1]);

    std::string line;

    int sum = 0;
    while(getline(input, line)) {
        sum += calNum(line);
    }

    std::cout << sum << std::endl;

    input.close();
    return EXIT_SUCCESS;
}