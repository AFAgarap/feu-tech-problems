#include <iostream>
#include <string>

int factorial(int n){
	return (n > 0) ? n * factorial(n - 1) : 1;
}

int input(std::string message){
	int x;
	std::cout << message;
	std::cin >> x;
	return x;
}

int main(){
	int n = input("Enter n: "), k = input("Enter k: ");
	std::cout << factorial(n) / (factorial(k) * factorial(n - k)) << std::endl;
	return 0;
}
