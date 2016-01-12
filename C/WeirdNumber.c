#include <stdio.h>
int main(){
	int number = 0;
	printf("Enter a number: ");
	scanf("%d", &number);
	printf(((number % 2 != 0 || number >= 5 && number <= 20) ? "Weird\n" : "Not Weird\n"));
	return 0;
}
