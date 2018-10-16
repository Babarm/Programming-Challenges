#include <stdio.h>

#define false 0
#define true 1
#define bool char

bool is_prime(int n);

int main() {
	printf("%d\n", 2);
	for(int i = 3; i < 100000; i += 2)
		if(is_prime(i))
			printf("%d\n", i);
	printf("\n");
	return 0;
}

bool is_prime(int n) {
	if(n <= 1)
		return false;
	else if(n == 2)
		return true;
	else if(n % 2 == 0)
		return false;
	for(int i = 3; i * i <= n; i += 2)
		if(n % i == 0)
			return false;
	return true;
}
