#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
	srand(time(NULL));

	int guess = 0, last_guess = 0;
	int num_guesses = 0;
	int value = (rand() % 100) + 1;

	while(1) {
		printf("Guess a number between 1 and 100: ");
		scanf("%d", &guess);
		num_guesses++;
		if(guess == last_guess)
			num_guesses--;
		last_guess = last_guess;

		if(guess < value) {
			printf("Too Low!\n");
		} else if(guess > value) {
			printf("Too High!\n");
		} else {
			printf("You got it!\n");
			printf("You needed %d guesses!\n", num_guesses);
			break;
		}
	}

	return 0;
}
