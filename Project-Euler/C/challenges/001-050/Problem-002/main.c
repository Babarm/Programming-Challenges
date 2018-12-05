#include "../../library/plibrary.h"

int main() {
    setlocale(LC_NUMERIC, "");

    uint64_t ans = 0;
    uint64_t a = 1, b = 1, fib = 2;

    uint64_t start = ns();

    do {
        ans += fib;
        a = b + fib;
        b = fib + a;
        fib = a + b;
    } while(fib <= 4000000);


    uint64_t end = ns();

    printf("Answer: %'lu\n", ans);

    char * timestamp = format_time(end - start);
    printf("Time elapsed: %s\n", timestamp);
    free(timestamp);

    return 0;
}
