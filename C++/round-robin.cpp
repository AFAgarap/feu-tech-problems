#include <iostream>
#include <sstream>
#include <string>

int input(std::string message);
std::string concat(std::string message, int number);

int main() {
	int temp = 0;
	int size = input("How many processes will you enter? ");

	int process[size][6];

	for (int index = 0; index < size; index++) {
		process[index][0] = input(concat("Enter arrival time for job #", index));
		process[index][1] = input(concat("Enter service time for job #", index));
		std::cout << "================================" << std::endl;
	}


	for (int index = 0; index < size - 1; index++) {
		for (int j = 0; j < size - index - 1; j++) {
			if (process[j][0] > process[j + 1][0]) {
				temp = process[j][0];
				process[j][0] = process[j + 1][0];
				process[j + 1][0] = temp;

				temp = process[j][1];
				process[j][1] = process[j + 1][1];
				process[j + 1][1] = temp;
			}
		}
	}

	for (int index = 0; index < size; index++) {
		std::cout << process[index][0] << " : " << process[index][1] << std::endl;
	}

	return 0;
}

int input(std::string message) {
	int number;
	std::cout << message;
	std::cin >> number;
	return number;
}

std::string concat(std::string message, int number) {
	std::stringstream ss;
	std::string s;
	ss << message << number << ": ";
	s = ss.str();
	return s;
}