#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define LIMIT 1024

void reverse(char * string, int len);
void swap(char * a, char * b);

int main() {
	char * sum = (char *)malloc(LIMIT * sizeof(char)); // Allocate space for sum
	memset(sum, 0 + '0', LIMIT); // Fill string with zeros

	char * buffer = (char *)malloc(50 * sizeof(char));

	scanf("%s", buffer);

	reverse(buffer, 50);

	int carry;
	int digit_sum;

	free(buffer);
	free(sum);
	return EXIT_SUCCESS;
}


void reverse(char * string, int len) {
	for(int i = 0; i < len / 2; i++) {
		swap(&string[i], &string[len - i - 1]);
	}
}

void swap(char * a, char * b) {
	char tmp = *a;
	*a = *b;
	*b = tmp;
}
