#include <iostream>
int factorial(int n){
	return (n > 0) ? n * factorial(n - 1) : 1;
}

int main(){
	int n = 0, k = 0;
	std::cout << "Enter n: ";
	std::cin >> n;
	std::cout << "Enter k: ";
	std::cin >> k;
	std::cout << factorial(n) / (factorial(k) * factorial(n - k)) << std::endl;
	return 0;
}
