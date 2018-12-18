#include "../../library/plibrary.h"

int main() {
    setlocale(LC_NUMERIC, "");
    
    uint64_t LIMIT = 600851475143L;

    uint64_t ans = 0;

    uint64_t start = ns();

    uint64_t i = 2;

    do {
        if(LIMIT % i == 0) {
            LIMIT /= i;
            ans = i;
        } else i++;
    } while(i * i < LIMIT);

    if(LIMIT > ans) {
        ans = LIMIT;
    }

    uint64_t end = ns();

    printf("Answer: %'lu\n", ans);

    char * timestamp = format_time(end - start);
    printf("Time elapsed: %s\n", timestamp);
    free(timestamp);

    return 0;
}
