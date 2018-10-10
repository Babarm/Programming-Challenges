#include "main.h"

/* Main entrypoint of program */
int main() {
	setlocale(LC_NUMERIC, "");

	int challenge_id;

	while(1) {
		get_id(&challenge_id);
		if(challenge_id == 0)
			break;
		run(challenge_id);
	}

	return EXIT_SUCCESS;
}

