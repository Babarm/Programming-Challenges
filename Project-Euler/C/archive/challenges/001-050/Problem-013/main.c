#include "../../library/plibrary.h"

int main() {
    setlocale(LC_NUMERIC, "");

    uint64_t ans = 0;

    FILE * file = fopen("data.txt", "r");
    if(file == NULL) {
        fprintf(stderr, "Unable to open file \"data.txt\" for reading!\n");
        exit(EXIT_FAILURE);
    }

    int digit_sums[52];
    memset(digit_sums, 0, 52 * sizeof(int));

    char * line = malloc(52);

    uint64_t start = ns();

    while(fgets(line, 52, file) != NULL)
        for(int i = 0; i < 50; i++)
            digit_sums[i] += (line[i] - '0');

    for(int i = 49; i >= 0; i--)
        digit_sums[i + 2] = digit_sums[i];
    digit_sums[0] = digit_sums[1] = 0;

    for(int i = 51; i > 0; i--) {
        int val = digit_sums[i] % 10;
        int carry = (digit_sums[i] - (val)) / 10;
        digit_sums[i - 1] += carry;
        digit_sums[i] = val;
    }

    for(int i = 0; i < 10; i++) {
        ans *= 10;
        ans += digit_sums[i];
    }

    uint64_t end = ns();

    printf("Answer: %'lu\n", ans);

    char * timestamp = format_time(end - start);
    printf("Time elapsed: %s\n", timestamp);
    free(timestamp);
    free(line);
    free(file);
    return 0;
}
