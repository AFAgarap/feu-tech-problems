/*
	If n is odd or if n is even and in between 6 and 20 (inclusive), print "Weird"
	If n is even and in between 2 and 5 (inclusive) or if n is even and > 20, print "Not Weird"
*/
#include <iostream>
int main(){
	int n = 0;
	std::cin >> n;
	std::cout << ((n % 2 != 0 || n >= 5 && n <= 20) ? "Weird" : "Not Weird") << std::endl;
	return 0;
}
