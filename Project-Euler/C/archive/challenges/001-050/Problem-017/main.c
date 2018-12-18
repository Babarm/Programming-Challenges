#include "../../library/plibrary.h"

int main() {
    setlocale(LC_NUMERIC, "");

    uint64_t ans = 0;

    uint64_t start = ns();

    char * string;
    for(int i = 1; i <= 1000; i++) {
        string = num2string(i);
        for(int j = 0; j < strlen(string); j++)
            if(string[j] != ' ')
                ans++;
        free(string);
    }

    uint64_t end = ns();

    printf("Answer: %'lu\n", ans);

    char * timestamp = format_time(end - start);
    printf("Time elapsed: %s\n", timestamp);
    free(timestamp);

    return 0;
}
