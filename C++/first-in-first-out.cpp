/*
*	Author : A.F. Agarap
*	First-In, First-out algorithm
*/


#include <iostream>
#include <sstream>
#include <string>

int input(std::string message);
std::string concat(std::string message, int number);

int main(){
	int temp, size = input("How many processes will you enter? ");

	int process[size][7];

	for (int i = 0; i < size; i++) {
		process[i][0] = input("Enter process number: ");
		process[i][1] = input(concat("Enter arrival time for job #", process[i][0]));
		process[i][2] = input(concat("Enter service time for job #", process[i][0]));
		std::cout << "================================" << std::endl;
	}

	for (int index = 0; index < size - 1; index++) {
		for (int j = 0; j < size - index - 1; j++) {
			if (process[j][1] > process[j + 1][1]) {
				temp = process[j][1];
				process[j][1] = process[j + 1][1];
				process[j + 1][1] = temp;

				temp = process[j][0];
				process[j][0] = process[j + 1][0];
				process[j + 1][0] = temp;

				temp = process[j][2];
				process[j][2] = process[j + 1][2];
				process[j + 1][2] = temp;
			}
		}
	}
	
	for (int i = 0; i < size; i++) {
		if (i == 0 || (process[i - 1][4] < process[i][1]) && i != 0) {
			process[i][3] = process[i][1];
		} else {
			// process[i][3] = (process[i - 1][4] > process[i][1]) ? process[i - 1][4] : process[i][1];
			process[i][3] = process[i - 1][4];
		}
		process[i][4] = process[i][3] + process[i][2];
	}

	for (int i = 0; i < size; ++i) {
		if (i == 0 && process[i][1] == 0) {
			process[i][5] = process[i][1];
			
		} else {
			process[i][5] = process[i][3] - process[i][1];
		}
	}

	for (int i = 0; i < size; i++) {
		process[i][6] = process[i][4] - process[i][1];
	}

	for (int i = 0; i < size; i++) {
		std::cout << "P #" << process[i][0] << "\tAT : " << process[i][1] << "\tBT : " << process[i][2] << "\tST : " << process[i][3] << "\tFT : " << process[i][4] << "\tWT : " << process[i][5] << "\tTAT : " << process[i][6] << std::endl;
	}	

	for (int i = 0; i < size; i++) {
		if (process[i][3] == process[i - 1][4]) {
			for (int j = 1; j < process[i][4] - process[i - 1][4]; j++) { std::cout << " - "; }
			std::cout << process[i][4] << " ";
		} else if (process[i][3] != process[i - 1][4] || i == 0) {
			std::cout << process[i][3];
			for (int j = 1; j < process[i][4] - process[i][3]; j++) { std::cout << " - "; }
			std::cout << process[i][4] << " ";
		}
		
	}
	std::cout << std::endl;
	// system("pause");
}

int input(std::string message){
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
	