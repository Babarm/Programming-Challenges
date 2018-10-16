#include <stdio.h>

int sum(int n);

int main() {
	int n;
	printf("Number: ");
	scanf("%d", &n);
	printf("Sum: %d\n", sum(n));
	return 0;
}

int sum(int n) {
	int sum = 0;
	for(int i = 1; i < n; i++)
		if(i % 3 == 0 || i % 5 == 0)
			sum += i;
	return sum;
}
