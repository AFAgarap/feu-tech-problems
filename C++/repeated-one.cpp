#include <bits/stdc++.h>
#include <iostream>
#include <sstream>
#include <string>

std::string concat(std::string number_str, int number);

int main() {
	std::string n = "0";
	int i = 0;
	int result = 0;

	for (int index = 1; index < 11; index++) {
		i = atoi(n.c_str());
		result = (i * 9) + index;
		n = concat(n, index);
		std::cout << i << " * 9 + " << index << " = " << result << std::endl;
	}

	return 0;
}

std::string concat(std::string number_str, int number) {
	std::stringstream ss;
	std::string s;
	ss << number_str << number;
	s = ss.str();
	return s;
}