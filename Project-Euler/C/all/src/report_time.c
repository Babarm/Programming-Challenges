#include "main.h"

/* Reports timestamp in a readable format */
void report_time(uint64_t span) {
	if(span >= 1e9) {
		printf("%'0.3f sec", (double)span / 1e9);
	} else if(span >= 1e6) {
		printf("%0.3f ms", (double)span / 1e6);
	} else if(span >= 1e3) {
		printf("%0.3f \u03BCs", (double)span / 1e3);
	} else {
		printf("%ld ns", span);
	}
	printf("\n");
}
