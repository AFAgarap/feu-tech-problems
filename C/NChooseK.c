#include <stdio.h>

int factorial(int n){
	return (n > 0) ? (n * factorial(n - 1)) : 1;
}

int input(char message[]){
	int x;
	printf("%s", message);
	scanf("%d", &x);
	return x;
}

int main(){
	int n = input("Enter n: "), k = input("Enter k: ");
	printf("%d\n", (factorial(n) / (factorial(k) * factorial(n - k))));
	return 0;
}
