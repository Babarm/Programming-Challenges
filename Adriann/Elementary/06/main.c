#include <stdio.h>

int sum(int n);
int factorial(int n);

int main() {
	int n, choice;

	printf("Number: ");
	scanf("%d", &n);

	printf("Sum (0) or Product (1)? ");
	scanf("%d", &choice);

	switch(choice) {
		case 0:
			printf("Sum: %d\n", sum(n));
			break;
		case 1:
			printf("Product: %d\n", factorial(n));
			break;
		default:
			printf("Invalid option!\n");
			break;
	}

	return 0;
}

int sum(int n) {
	return (n * (n + 1)) >> 1;
}

int factorial(int n) {
	int product = 1;
	for(int i = n; i > 1; i--)
		product *= i;
	return product;
}
