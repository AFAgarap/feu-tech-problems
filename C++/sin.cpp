// Maclaurin series for sin(x)
#include <iostream>
#include <cmath>

int factorial(int n);

int main(){
	std::cout << "10th degree of Maclaurin series, sin(x)\nEnter value of x (in Radians): ";
	double x;
	std::cin >> x;
	double answer = x; int i = 1, j = 1;
	while (i < 10){
		if (i == 1){
			answer -= pow(x, (j + 2)) / factorial(j + 2);
		}else if (i % 2 == 0){
			answer += pow(x, (j + 2)) / factorial(j + 2);
		}else if (i % 2 != 0){
			answer -= pow(x, (j + 2)) / factorial(j + 2);
		}
		i += 1; j += 2;
	}
	std::cout << answer << std::endl;
	return 0;
}

int factorial(int number){
	return (number == 0) ? 1 : number * factorial(number - 1);
}
