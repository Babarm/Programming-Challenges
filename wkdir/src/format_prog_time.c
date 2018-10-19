#include "engine.h"

/* Formats a nanosecond timestamp into a readable format */
/* FOR APPLICATION */
void format_prog_time(char * dest, uint64_t * span) {
	int hr  = (int)(*span / 3600000000000);
	*span %= 3600000000000;
	int min = (int)(*span / 60000000000  );
	*span %= 60000000000;
	int sec = (int)(*span / 1000000000   );
	sprintf(dest, "%02d:%02d:%02d", hr, min, sec);
	return;
}
