#include <stdio.h>

int input(char message[]){
	int x;
	printf("%s", message);
	scanf("%d", &x);
	return x;
}

int main(){
	int testCases = input("Enter number of test cases: "), number, butts, count, i;

	for(i = 0; i < testCases; i = i + 1){
		number = input("Enter number of cigarettes: ");
		butts = input("Enter number of butts: ");
		count = number;
		while(number >= butts){
			count += number / butts;
			number /= butts;
		}
		printf("Count: %d\n", count);
	}
	return 0;
}
