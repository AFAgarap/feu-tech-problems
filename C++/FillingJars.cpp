#include <iostream>
#include <string>

int input(std::string message){
	int x = 0;
	std::cout << message;
	std::cin >> x;
	return x;
}

int main(){
	int answer = 0, n = input("Enter n: "), m = input("Enter m: ");
	for (int i = 0; i < m; i++) {
		answer += (((input("Enter b: ") - input("Enter a: ")) + 1) * input("Enter k: "));
	}
	std::cout << (answer / n) << std::endl;
}