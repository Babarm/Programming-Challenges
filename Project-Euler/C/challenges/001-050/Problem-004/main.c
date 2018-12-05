#include "../../library/plibrary.h"

int main() {
    setlocale(LC_NUMERIC, "");

    uint64_t ans = 0;

    uint64_t start = ns();

    for(int a = 999; a >= 100; a--) {
        int b, db;
        if(a % 11 == 0) {
            b = 999;
            db = 1;
        } else {
            b = 990;
            db = 11;
        }

        for(; b >= a; b -= db) {
            if(a * b <= ans) break;
            if(is_palindrome_int(a * b)) ans = a * b;
        }
    }

    uint64_t end = ns();

    printf("Answer: %'lu\n", ans);

    char * timestamp = format_time(end - start);
    printf("Time elapsed: %s\n", timestamp);
    free(timestamp);

    return 0;
}
