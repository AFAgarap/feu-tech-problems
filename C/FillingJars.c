#include <stdio.h>
int input(char msg[50]){
	int x = 0;
	printf("%s", msg);
	scanf("%d", &x);
	return x;
}
int main(){
	int answer = 0, n = input("Enter n: "), m = input("Enter m: "), i;
	for(i = 0; i < m; i++){
		answer = answer + (((input("Enter b: ") - input("Enter a: ")) + 1) * input("Enter k: "));
	}
	printf("%d\n", (answer / n));
	return 0;
}
