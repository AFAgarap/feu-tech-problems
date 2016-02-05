#include <stdio.h>

int main(){
	int x = 0, total = 0, i, j;
	scanf("%d", &x);
	for (i = 1, j = 0; j < x; j++){
		if (j % 2 != 0) i++;
		total += i;
	}
	printf("%d\n", total);
}