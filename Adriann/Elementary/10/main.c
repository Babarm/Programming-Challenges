#include <stdio.h>
#include <time.h>

int main() {
	time_t timer;
	struct tm* tm_info;
	char year_str[5];
	int year = 0;
	time(&timer);
	tm_info = localtime(&timer);
	strftime(year_str, 5, "%Y", tm_info);
	for(int i = 0; i < 4; i++) {
		year *= 10;
		year += (year_str[i] - '0');
	}
	
	int leap = 0;
	for(int i = 0; i < 20;) {
		leap = 0;
		if(year % 4 == 0)
			leap = 1;
		if(year % 100 == 0)
			leap = 0;
		if(year % 400 == 0)
			leap = 1;
		if(leap) {
			printf("%d: %d\n", i + 1, year);
			i++;
		}
		year++;
	}

	return 0;
}
