#include <iostream>
int main(){
	std::cout << "Enter number of test cases: ";
	int testCases = 0, number = 0, butts = 0, count = 0;
	std::cin >> testCases;

	for(int i = 0; i < testCases; i++){
		std::cout << "Enter number of cigarettes: ";
		std::cin >> number;
		std::cout << "Enter number of butts: ";
		std::cin >> butts;
		count = number;
		while(number >= butts){
			count += number / butts;
			number /= butts;
		}
		std::cout << count << std::endl;
	}

	return 0;
}
