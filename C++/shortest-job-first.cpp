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

	// [[0, 5], [1, 3], [2, 8], [3, 6]]
	/*
		5 3 8 6
			5 < 3 : swap 3 and 5	([0] < [1])
		3 5 8 6
			5 < 8 : as is 			([1] < [2])
		3 5 8 6	
		3 5 8 6
			8 < 6 : 				([2] < [3])
		3 5 8 6
			6 < 3 :					([3] < [0])
		3 5 8 6
			6 < 5 :					([3] < [1])
		3 5 8 6
			6 < 8 :					([3] < [2])
	*/

	for (int index = 1; index < size; index++) {
		if (process[index - 1][1] > process[index][1]) {
			temp = process[index][1];
			process[index][1] = process[index - 1][1];
			process[index - 1][1] = temp;

			temp = process[index][0];
			process[index][0] = process[index - 1][0];
			process[index - 1][0] = temp;
		}
	}

	for (int index = 0; index < size; index++) {
		std::cout << process[index][0] << " : " << process[index][1] << std::endl;
	}

	return 0;
}

// [[0, 5], [1, 3], [2, 8], [3, 6]]

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