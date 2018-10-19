#include "engine.h"

extern int challenge_runner_running;

// Runs the specified challenge
void * run_challenge(void * id) {
	challenge_runner_running = 0;
	return NULL;
}
