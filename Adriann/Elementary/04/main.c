#include <stdio.h>

int sum(int n);

int main() {
	int n;
	printf("Number: ");
	scanf("%d", &n);
	printf("Sum of all numbers 1 to %d: %d\n", n, sum(n));
	return 0;
}

int sum(int n) {
	return (n * (n + 1)) >> 1;
}
