#include "../../library/plibrary.h"

int main() {
    setlocale(LC_NUMERIC, "");

    uint64_t ans = 3;
    int num_primes = 1;

    uint64_t start = ns();

    do {
        if(is_prime((int)ans)) num_primes++;
        if(num_primes == 10001) break;
        ans += 2;
    } while(true);

    uint64_t end = ns();

    printf("Answer: %'lu\n", ans);

    char * timestamp = format_time(end - start);
    printf("Time elapsed: %s\n", timestamp);
    free(timestamp);

    return 0;
}
