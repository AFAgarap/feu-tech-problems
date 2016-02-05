#include <iostream>
#include <string>

int input(std::string msg){
	int x = 0;
	std::cout << msg;
	std::cin >> x;
	return x;
}

int main(){
	int earthDays = input("Enter input for Earth: ");
	int marsDays = input("Enter input for Mars: ");
	int counter = 0;
	while (true){
		if (marsDays % 687 == 0 && earthDays % 365 == 0) break;
		counter++; marsDays++; earthDays++;
	}
	std::cout << counter << std::endl;
}