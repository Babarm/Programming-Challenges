#include <stdio.h>
#include <stdlib.h>

void factorial(int n, char* buffer);

int main() {
	char * buffer = malloc(256 * sizeof(char));

	factorial(100, buffer);

	free(buffer);
	return EXIT_SUCCESS;
}

void factorial(int n, char* buffer) {
	int counter, carry, i;
	buffer[0] = 1;
	counter = 0;
	for(; n >= 2; n--) {
		carry = 0;
		for(i = 0; i <= counter; i++) {
			carry += (buffer[i] * n);
			buffer[i] = carry % 10;
			carry /= 10;
		}
		while(carry > 0) {
			buffer[++counter] = carry % 10;
			carry /= 10;
		}
	}

	for( i = counter; i >= 0; i--) {
		printf("%d", buffer[i]);
	}
	printf("\n");
}
