#include <stdio.h>
int main(){
	int i, j, k;
	for (i = 1; i <= 10; i++){
		for (k = 10; k >= 0; k--){
			printf((k + i <= 10) ? " " : "");
		}
		for (j = 1; j < i; j++){
			printf("%d %s", j, " ");
		}
		printf("\n");
	}
}
