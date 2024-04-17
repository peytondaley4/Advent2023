#include <fstream>
#include <iostream>
#include <algorithm>
#include <map>
#include <string>

int calNum(std::string line, std::map<int, std::string> norm, std::map<int, std::string> backw) {
    std::string rev = line;
    reverse(rev.begin(), rev.end());

    int findex, lindex, fnum, lnum, first, last;

    first = line.find_first_of("0123456789");
    last = rev.find_first_of("0123456789");
    fnum = int(line[first] - '0');
    lnum = int(rev[last] - '0');

    for (int i = 1; i < 10; i++) {
        findex = line.find(norm[i]);
        if (findex == std::string::npos) continue;
        if (findex < first) {
            first = findex;
            fnum = i;
        }
    }

    for (int i = 1; i < 10; i++) {
        lindex = rev.find(backw[i]);
        if (lindex == std::string::npos) continue;
        if (lindex < last) {
            last = lindex;
            lnum = i;
        }
    }

    return fnum*10 + lnum;
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cout << "Improper arguments, expects file name" << std::endl;
        return EXIT_FAILURE;
    }

    std::ifstream input;
    input.open(argv[1]);

    std::string line;

    std::map<int, std::string> norm = {
        {1, "one"},
        {2, "two"},
        {3, "three"},
        {4, "four"},
        {5, "five"},
        {6, "six"},
        {7, "seven"},
        {8, "eight"},
        {9, "nine"}
    };

    std::map<int, std::string> backw = {
        {1, "eno"},
        {2, "owt"},
        {3, "eerht"},
        {4, "ruof"},
        {5, "evif"},
        {6, "xis"},
        {7, "neves"},
        {8, "thgie"},
        {9, "enin"}
    };

    int sum = 0;
    while(getline(input, line)) {
        sum += calNum(line, norm, backw);
    }

    std::cout << sum << std::endl;

    input.close();
    return EXIT_SUCCESS;
}