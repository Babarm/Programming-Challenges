#include <stdio.h>

#define MAX_LENGTH 64
int main() {
	char name[MAX_LENGTH];
	printf("What is your name?\n");
	scanf("%[^\n]%*c", name);
	printf("Hello %s!\n", name);
}
