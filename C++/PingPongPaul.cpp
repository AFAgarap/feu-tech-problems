#include <iostream>
int main(){
	int n = 0, p = 0, q = 0;
	std::cout << "Enter n: ";
	std::cin >> n;
	std::cout << "Enter p: ";
	std::cin >> p;
	std::cout << "Enter q: ";
	std::cin >> q;
	std::cout << ((((p + q) / n) % 2 == 0) ? "paul" : "opponent") << std::endl;
	return 0;
}
