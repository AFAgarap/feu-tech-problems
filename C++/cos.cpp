// Maclaurin series for cos(x)
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
	if (n > 1) {
		return n * factorial(n - 1);
	} else {
		return 1;
	}
}