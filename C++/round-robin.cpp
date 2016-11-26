#include <iostream>
#include <sstream>
#include <string>

int input(std::string message);
std::string concat(std::string message, int number);

int main() {
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