#include <stdio.h>
int input(char message[]){
	int x;
	printf("%s", message);
	scanf("%d", &x);
	return x;
}
int main(){
	int n = input("Enter n: "), p = input("Enter p: "), q = input("Enter q: ");
	printf(((((p + q) / n) % 2 == 0) ? "paul\n" : "opponent\n"));
	return 0;
}
