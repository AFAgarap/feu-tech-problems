#include <stdio.h>
int main(){
	printf("Enter number of test cases: ");
	int testCases = 0, number = 0, butts = 0, count = 0, i;
	scanf("%d", &testCases);

	for(i = 0; i < testCases; i = i + 1){
		printf("Enter number of cigarettes: ");
		scanf("%d", &number);
		printf("Enter number of butts: ");
		scanf("%d", &butts);
		count = number;
		while(number >= butts){
			count += number / butts;
			number /= butts;
		}
		printf("Count: %d\n", count);
	}
	return 0;
}
