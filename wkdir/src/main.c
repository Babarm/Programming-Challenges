#include "engine.h"

int main() {
	uint64_t prog_start, prog_end, prog_span;

	/* Starting timestamp */
	prog_start = ns();

	/* Main loop of program */
	__init__();

	/* Ending timestamp */
	prog_end = ns();

	/* Calculate timespan */
	prog_span = prog_end - prog_start;

	/* Report how long the program was running */
	char * time_description = malloc(64 * sizeof(char));
	memset(time_description, '\0', 64);
	format_prog_time(time_description, &prog_span);
	printf("Runtime %s\n", time_description);
	free(time_description);

	return EXIT_SUCCESS;
}
