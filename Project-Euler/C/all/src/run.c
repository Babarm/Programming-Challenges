#include "challenges.h"
#include "main.h"

/* Runs the specified challenge */
void run(int id) {
	int64_t ans = 0;
	uint64_t start, end;
	start = ns();
	switch(id) {
		case 1:
			ans = challenge_001();
			break;
		default:
			printf("Challenge #%d not found!\n\n", id);
			return;
	}
	end = ns();

	printf("Answer: %'ld\n", ans);
	report_time(end - start);
}
