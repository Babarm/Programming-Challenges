#include <stdio.h>
#include <stdlib.h>

int main() {
	int num;
	int den;
	double sum = 0.0;
	for(int k = 1; k <= 1000000; k++) {
		/* num: (-1) ^ (k + 1) */
		if(k << 31 == 0) num = -1; /* k is even (k + 1 is odd) */
		else num = 1; /* k is odd (k + 1 is even) */

		/* den: 2k - 1 */
		den = (2 * k) - 1;
		sum += (double)num / (double)den;
	}
	printf("%.50f\n", sum);
	return EXIT_SUCCESS;
}
