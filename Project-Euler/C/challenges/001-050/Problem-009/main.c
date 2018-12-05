#include "../../library/plibrary.h"

int main() {
    setlocale(LC_NUMERIC, "");

    uint64_t ans = 0;

    uint64_t start = ns();
    
    for(int a = 3; a < 333; a++) {
        for(int b = a + 1; b < 500; b++) {
            int c = 1000 - a - b;
            if(c * c == a * a + b * b) ans = a * b * c;
        }
    }

    uint64_t end = ns();

    printf("Answer: %'lu\n", ans);

    char * timestamp = format_time(end - start);
    printf("Time elapsed: %s\n", timestamp);
    free(timestamp);

    return 0;
}
