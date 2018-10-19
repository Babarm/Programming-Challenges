#include "engine.h"

/* Formats a nanosecond timestamp into a readable format */
/* FOR CHALLENGE */
void format_time(char * dest, uint64_t * span) {
	if(*span >= 60000000000) {
		sprintf(dest, "%d min", (int)(*span / 60000000000));
		*span %= 60000000000;
		if(*span >= 1000000000) {
			sprintf(dest + strlen(dest), "%0.3f sec", (double)*span / 1000000000);
		}
		return;
	}

	if(*span >= 1000000000) {
		sprintf(dest, "%0.3f sec", (double)*span / 1000000000);
	} else if(*span >= 1000000) {
		sprintf(dest, "%0.3f ms", (double)*span / 1000000);
	} else if(*span >= 1000) {
		sprintf(dest, "%0.3f \u03BCs", (double)*span / 1000);
	} else {
		sprintf(dest, "%lu", *span);
	}
	return;
}
