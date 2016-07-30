// Maclaurin series for arctan(x)
#include <iostream>
#include <string>
#include <math.h>

double input(std::string message){
	double x = 0;
	std::cout << message;
	std::cin >> x;
	return x;
}

int main(){
	double x = input("Enter x: ");
	double k = input("Enter k: ");
	double answer = x;
	for (int i = 1, j = 1; i < k; i++, j += 2){
		if (i == 1){
			answer -= pow(x, (j + 2)) / (j + 2);
		}else if (i % 2 == 0){
			answer += pow(x, (j + 2)) / (j + 2);
		}else if (i % 2 != 0){
			answer -= pow(x, (j + 2)) / (j + 2);
		}
	}
	std::cout << "Answer: " << answer << std::endl;
}
