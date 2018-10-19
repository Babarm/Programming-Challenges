#include "engine.h"

int challenge_runner_running = 0;
int run_challenges = 1;

/* Main Loop of Application */
void __init__() {
	setlocale(LC_NUMERIC, "");

	while(run_challenges) {

		int valid, id, gc;
		printf("Challenge ID: ");
		valid = scanf("%d", &id);
		while(valid != 1) {
			while((gc = getchar()) != EOF && gc != '\n');
			printf("Challenge ID: ");
			valid = scanf("%d", &id);
		}

		/* Spawn a thread to run the specified challenge. */
		pthread_t challenge_runner;
		challenge_runner_running = 1;
		pthread_create(&challenge_runner, NULL, run_challenge, (void *)(&id));

		/* Wait until the challenge is done running, showing the user that it is still running */
		int i = 0;
		for(;;i++) {
			if(i % 4 == 0)
				printf("Running       \r");
			else if(i % 4 == 1)
				printf("Running .     \r");
			else if(i % 4 == 2)
				printf("Running . .   \r");
			else {
				printf("Running . . . \r");
				i = -1;
			}
			if(!challenge_runner_running) {
				printf("Running . . . \n");
				break;
			}

			fflush(stdout);
			usleep(250000);
		}

		/* Join the thread */
		pthread_join(challenge_runner, NULL);
		run_challenges = 0;
	}

	return;
}


/* ================================================================================================================== */

void * run_challenge(void * id) {
	challenge_runner_running = 0;
	return NULL;
}


/* ================================================================================================================== */


/* Gets nanosecond timestamp */
uint64_t ns() {
	static uint64_t is_init = 0;
#if defined(__APPLE__)
	static mach_timebase_info_data_t info;
	if( 0 == is_init ) {
		mach_timebase_info(&info);
		is_init = 1;
	}
	uint64_t now;
	now = mach_absolute_time();
	now *= info.numer;
	now /= info.denom;
	return now;
#elif defined(__linux)
	static struct timespec linux_rate;
	if( 0 == is_init ) {
		clock_getres(CLOCKID, &linux_rate);
		is_init = 1;
	}
	uint64_t now;
	struct timespec spec;
	clock_gettime(CLOCKID, &spec);
	now = spec.tv_sec * 1.0e9 + spec.tv_nsec;
	return now;
#elif defined(_WIN32)
	static LARGE_INTEGER win_frequency;
	if( 0 == is_init ) {
		QueryPerformanceFrequency(&win_frequency);
		is_init == 1;
	}
	LARGE_INTEGER now;
	QueryPerformanceCounter(&now);
	return (uint64_t) ((1e9 * now.QuadPart) / win_frequency.QuadPart);
#endif
}


/* ================================================================================================================== */


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


/* ================================================================================================================== */


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
