// Prints number pyramid from 1-9
#include <iostream>
int main(){
	for (int i = 1; i <= 10; i++){
		for (int k = 10; k >= 0; k--){
			std::cout << ((k + i <= 10) ? " " : "");
		}
		for (int j = 1; j < i; j++){
			std::cout << j << " ";
		}
		std::cout << "\n";		
	}
}
