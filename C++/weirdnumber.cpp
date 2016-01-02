#include <iostream>
int main(){
	int n = 0;
	std::cin >> n;
	std::cout << ((n % 2 != 0 || n >= 5 && n <= 20) ? "Weird" : "Not Weird") << std::endl;
	return 0;
}
