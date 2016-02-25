#include <iostream>
#include <string>

int main(){
	int numString, numQuery;

	std::cin >> numString;
	
	std::string arr[numString];

	for (int i = 0; i < numString; i++){
		std::cin >> arr[i];
	}

	std::cin >> numQuery;
	
	int count[numQuery];

	for (int i = 0; i < numQuery; i++){
		int l, r;
		std::string s;
		std::cin >> l >> r >> s;

		int counter = 0;
		
		for (int j = (l - 1); j < r; j++){
			counter += (s == arr[j]) ? 1 : 0;
		}
		count[i] = counter;
	}

	for (int i = 0; i < numQuery; i++){
		std::cout << count[i] << std::endl;
	}
}