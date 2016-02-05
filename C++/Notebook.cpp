#include <iostream>

int main(){
	int x = 0, total = 0;
	std::cin >> x;
	for (int i = 1, j = 0; j < x; j++){
		if (j % 2 != 0) i++;
		total += i;
	}
	std::cout << total << std::endl;
}