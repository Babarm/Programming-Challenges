#include <stdio.h>
#include <stdlib.h>

int main() {
	int ans = 0;
	int *ans_ptr = &ans;
	printf("Address: 0x%llX\n", (unsigned long long)&ans);
	printf("Value: %d\n", *(&ans));
	*(ans_ptr) = 1;
	printf("Value: %d\n", ans);
	return EXIT_SUCCESS;
}
