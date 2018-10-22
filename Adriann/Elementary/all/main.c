#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int sum(int n);
int sum_three_five(int n);
int factorial(int n);

int main() {
	/* Variables used for the program */
	/* ============================== */

	/* Character buffer to allow user input */
	const int MAX_SIZE = 128;
	char * buffer = malloc(MAX_SIZE * sizeof(char));
	memset(buffer, '\0', MAX_SIZE * sizeof(char));

	/* Integers to be used as flags for valid input */
	int valid_input, garbage_collector;

	/* Integers used for input */
	int n, choice = 0;

	
	/*
	printf("[ 1] Hello World!\n\n");


	printf("[ 2] What is your name? ");
	valid_input = scanf("%[^\n]%*c", buffer);
	printf("     Hello %s!\n\n", buffer);


	printf("[ 3] ");
	if(strncmp(buffer, "Alice", strlen("Alice")) == 0 || strncmp(buffer, "Bob", strlen("Bob")) == 0)
		printf("Hello %s!\n\n", buffer);
	else
		printf("I'm sorry, I am not familiar with that name.\n\n");


	printf("[ 4] Please enter a number: ");
	valid_input = scanf("%d", &n);
	while(valid_input != 1) {
		while((garbage_collector = getchar()) != EOF && garbage_collector != '\n');
		printf("Invalid input.\n");
		printf("[ 4] Please enter a number: ");
		valid_input = scanf("%d", &n);
	}
	printf("     Sum of all numbers 1 to %d: %d\n\n", n, sum(n));


	printf("[ 5] Please enter a number: ");
	valid_input = scanf("%d", &n);
	while(valid_input != 1) {
		while((garbage_collector = getchar()) != EOF && garbage_collector != '\n');
		printf("Invalid input.\n");
		printf("[ 5] Please enter a number: ");
		valid_input = scanf("%d", &n);
	}
	printf("     Sum of all numbers 1 to %d that are multiples of 3 OR 5: %d\n\n", n, sum_three_five(n));


	printf("[ 6] Please enter a number: ");
	valid_input = scanf("%d", &n);
	while(valid_input != 1) {
		while((garbage_collector = getchar()) != EOF && garbage_collector != '\n');
		printf("Invalid input.\n");
		printf("[ 6] Please enter a number: ");
		valid_input = scanf("%d", &n);
	}
	printf("     Sum (1) or Product (2): ");
	valid_input = scanf("%d", &choice);
	if(choice < 1 || choice > 2)
		valid_input = 0;
	while(valid_input != 1) {
		while((garbage_collector = getchar()) != EOF && garbage_collector != '\n');
		printf("Invalid input.\n");
		printf("     Sum (1) or Product (2): ");
		valid_input = scanf("%d", &choice);
		if(choice < 1 || choice > 2)
			valid_input = 0;
	}
	if(choice == 1)
		printf("     Sum of all numbers 1 to %d: %d\n\n", n, sum(n));
	else
		printf("     Product of all numbers 1 to %d: %d\n\n", n, factorial(n));
	*/

	printf("[ 7]   |  1|  2|  3|  4|  5|  6|  7|  8|  9| 10| 11| 12|\n");
	printf("     --+---+---+---+---+---+---+---+---+---+---+---+---+\n");
	for(int i = 1; i <= 12; i++) {
		if(i < 10)
			printf(" ");
		printf("     %d|", i);
		for(int j = 1; j <= 12; j++) {
			int prod = i * j;
			if(prod >= 100)
				printf("%d|", prod);
			else if(prod >= 10)
				printf(" %d|", prod);
			else
				printf("  %d|", prod);
		}
		printf("\n     --+---+---+---+---+---+---+---+---+---+---+---+---+\n");
	}
	

	free(buffer);
	return EXIT_SUCCESS;
}

int sum(int n) {
	return (n * (n + 1)) >> 1;
}

int sum_three_five(int n) {
	int sum = 0;
	for(int i = 0; i <= n; i++)
		if(i % 3 == 0 || i % 5 == 0)
			sum += i;
	return sum;
}

int factorial(int n) {
	int prod = 1;
	for(int i = 2; i <= n; i++) {
		prod *= i;
	}
	return prod;
}
