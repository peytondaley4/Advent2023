#include <iostream>
#include <fstream>
#include <string>

int main(int argc, char* argv[]) {
    std::fstream input_file;
    input_file.open("input.txt");

    std::string buff;

    while(getline(input_file, buff, ':')) {
        std::cout << buff << std::endl;
        while (getline(input_file, buff, ';')) {
            std::cout << buff << std::endl;
        }
    }
}