#include <stdio.h>
#include <string.h>

#define MAX 64
int main() {
	char name[MAX];

	printf("Name: ");
	scanf("%[^\n]%*c", name);

	if (strcmp(name, "Alice") == 0 || strcmp(name, "Bob") == 0) {
		printf("Hello %s!\n", name);
	}
	return 0;
}
