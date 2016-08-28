#include <iostream>
#include <sstream>
#include <string>

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

int main(){
	int temp, size = input("How many processes will you enter? ");

	int process[size], arrivalTime[size], burstTime[size], startTime[size], finishedTime[size], waitingTime[size];

	for (int i = 0; i < size; i++) {
		process[i] = input("Enter process number: ");
	}

	for (int i = 0; i < size; i++) {
		arrivalTime[i] = input(concat("Enter arrival time for process number ", process[i]));
	}

	for (int i = 0; i < size; i++) {
		burstTime[i] = input(concat("Enter burst time for process number ", process[i]));
	}

	for(int i = 0; i < size; i++) {
		for(int j = 0; j < size - 1; j++) {
			if(arrivalTime[j] > arrivalTime[j + 1]) {
				temp = arrivalTime[j];
				arrivalTime[j] = arrivalTime[j + 1];
				arrivalTime[j + 1] = temp;

				temp = burstTime[j];
				burstTime[j] = burstTime[j + 1];
				burstTime[j + 1] = temp;

				temp = process[j];
				process[j] = process[j + 1];
				process[j + 1] = temp;
			}
		}
	}

	for (int i = 0; i < size; i++) {
		if (i == 0) {
			startTime[i] = arrivalTime[i];
		} else {
			startTime[i] = (finishedTime[i - 1] > arrivalTime[i]) ? finishedTime[i - 1] : arrivalTime[i];
		}
		finishedTime[i] = startTime[i] + burstTime[i];
	}

	for (int i = 0; i < size; ++i) {
		if (i == 0 && arrivalTime[i] == 0) {
			waitingTime[i] = arrivalTime[i];
		} else {
			waitingTime[i] = startTime[i] - arrivalTime[i];
		}
	}

	for (int i = 0; i < size; i++) {
		std::cout << "P #" << process[i] << "\tAT : " << arrivalTime[i] << "\tBT : " << burstTime[i] << "\tST : " << startTime[i] << "\tFT : " << finishedTime[i] << "\tWT : " << waitingTime[i] << std::endl;
	}	

	for (int i = 0; i < size; i++) {
		if (i == 0) {
			std::cout << startTime[i];
			for (int j = 0; j < finishedTime[i] - startTime[i]; j++) { std::cout << " - "; }
			std::cout << finishedTime[i] << " ";
		} else if (startTime[i] == finishedTime[i - 1]) {
			for (int j = 0; j < finishedTime[i] - finishedTime[i - 1]; j++) { std::cout << " - "; }
			std::cout << finishedTime[i] << " ";
		} else {
			std::cout << startTime[i];
			for (int j = 0; j < finishedTime[i] - startTime[i]; j++) { std::cout << " - "; }
			std::cout << finishedTime[i] << " ";
		}
	}
	std::cout << std::endl;
}
