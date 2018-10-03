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

void clear();

int abs(int val);

int run();

int main(int argc, char **argv);
