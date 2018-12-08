#include "../../library/plibrary.h"

#define MAXSIZE 256

int main() {
    setlocale(LC_NUMERIC, "");

    uint64_t ans = 0;

    char * factorial = malloc(MAXSIZE);
    memset(factorial, 0, MAXSIZE);

    int N = 100, carry = 0, x = 0, max_index = 0;

    uint64_t start = ns();

    factorial[0] = 1;
    max_index++;

    for(int i = 1; i <= N; i++) {
        for(int j = 0; j < max_index; j++) {
            x = factorial[j] * i + carry;
            factorial[j] = x % 10;
            carry = x / 10;
        }
        while(carry > 0) {
            factorial[max_index] = carry % 10;
            carry /= 10;
            max_index++;
        }
    }

    for(int i = max_index - 1; i >= 0; i--) {
        ans += factorial[i];
    }

    uint64_t end = ns();

    printf("Answer: %'lu\n", ans);

    char * timestamp = format_time(end - start);
    printf("Time elapsed: %s\n", timestamp);
    free(timestamp);

    free(factorial);

    return 0;
}
