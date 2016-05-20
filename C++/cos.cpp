#include <iostream>
#include <cmath>

int factorial(int n);

int main(){
	std::cout << "10th degree of Maclaurin series, cos(x)\nEnter value of x (in Radians): ";
	double x;
	std::cin >> x;
	double answer = x; int i = 1, j = 2;
	while(i < 10 && j <= 10){
		if (i % 2 == 0){
			answer += pow(x, j) / factorial(j);
		}else if (i % 2 != 0){
			answer -= pow(x, j) / factorial(j);
		}
		i += 1; j += 2;
	}
	std::cout << answer << std::endl;
	return 0;
}

int factorial(int n){
	return (n == 0) ? 1 : n * factorial(n - 1);
}
