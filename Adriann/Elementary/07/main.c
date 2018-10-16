#include <stdio.h>

int main() {
	int prod;
	printf("   |   1 |   2 |   3 |   4 |   5 |   6 |   7 |   8 |   9 |  10 |  11 |  12 |\n");
	printf("---+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+\n");
	for(int i = 1; i <= 12; i++) {
		if(i >= 10)
			printf(" %d|", i);
		else
			printf("  %d|", i);
		for(int j = 1; j <= 12; j++) {
			prod = i * j;
			if(prod >= 100)
				printf(" %d |", prod);
			else if(prod >= 10)
				printf("  %d |", prod);
			else
				printf("   %d |", prod);
		}
		printf("\n---+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+\n");
	}
	return 0;
}
