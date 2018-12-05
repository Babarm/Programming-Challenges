#include "../../library/plibrary.h"

#define LIMIT 1000000

int main() {
    setlocale(LC_NUMERIC, "");

    uint64_t ans = 0;
    int longest_chain = 0;

    uint64_t start = ns();
    
    for(uint64_t i = 1; i < LIMIT; i += 2) {
        int chain = 0;
        uint64_t n = i;
        while(n != 1) {
            chain++;
            if(n % 2 == 0)
                n >>= 1;
            else
                n = 3 * n + 1;
        }
        if(chain > longest_chain) {
            ans = i;
            longest_chain = chain;
        }
    }

    uint64_t end = ns();

    printf("Answer: %'lu\n", ans);

    char * timestamp = format_time(end - start);
    printf("Time elapsed: %s\n", timestamp);
    free(timestamp);

    return 0;
}
