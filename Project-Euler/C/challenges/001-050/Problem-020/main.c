#include "../../library/plibrary.h"

int main() {
    setlocale(LC_NUMERIC, "");

    uint64_t ans = 0;

    uint64_t start = ns();

    char * digits = malloc(1024);
    sprintf(digits, "%.0f", factorial(100));
    printf("%s\n", digits);
    /*
    for(int i = 0 ;; i++) {
        if(digits[i] == '\0') break;
        ans += (digits[i] - '0');
    }
    */

    uint64_t end = ns();

    printf("Answer: %'lu\n", ans);

    char * timestamp = format_time(end - start);
    printf("Time elapsed: %s\n", timestamp);
    free(timestamp);

    return 0;
}
