#include <locale.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/time.h>
#include <time.h>

struct timedef {
	time_t tv_sec;
	long   tv_nsec;
};

int get_weekday(int day, int month, int year);

void clear();

size_t run();

int main(int argc, char **argv);
