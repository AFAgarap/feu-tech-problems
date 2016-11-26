#include <cmath>
#include <iostream>
#include <string>

int factorial(int number);
float input(std::string message);

int main() {
	float x = input("Enter value of x: ");
	float answer = 1, index = 1;

	while (index <= 10) {
		answer += pow(x, index) / factorial(index);
		index += 1;
	}

	std::cout << answer << std::endl;

	return 0;
}

int factorial(int number) {
	if (number > 0) {
		return number * factorial(number - 1);
	} else {
		return 1;
	}
}

float input(std::string message) {
	float number = 0.0;
	std::cout << message;
	std::cin >> number;
	return number;
}