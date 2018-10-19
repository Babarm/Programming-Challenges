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
			/* Print various stages of updates to the screen */
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

			if(!challenge_runner_running) { /* Break if the thread running the challenge is done running */
				printf("Running . . . \n");
				break;
			}

			fflush(stdout); /* Flush the stream (ensures the printf shows up) */
			usleep(250000); /* Sleep for 250 milliseconds */
		}

		/* Join the thread */
		pthread_join(challenge_runner, NULL);
		run_challenges = 0;
	}

	return;
}
