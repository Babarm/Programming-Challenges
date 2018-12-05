#include "../../library/plibrary.h"

int main() {
    setlocale(LC_NUMERIC, "");

    uint64_t ans = 0;
    int t[] = {0,3,2,5,0,3,5,1,4,6,2,4};

    uint64_t start = ns();

    for(int year = 1901; year <= 2000; year++) {
        for(int month = 1; month <= 12; month++) {
            int year_calc = year - (month < 3);
            if((year_calc + year_calc / 4 - year_calc / 100 + year_calc / 400 + t[month - 1] + 1) % 7 == 0)
                ans++;
        }
    }

    uint64_t end = ns();

    printf("Answer: %'lu\n", ans);

    char * timestamp = format_time(end - start);
    printf("Time elapsed: %s\n", timestamp);
    free(timestamp);

    return 0;
}
