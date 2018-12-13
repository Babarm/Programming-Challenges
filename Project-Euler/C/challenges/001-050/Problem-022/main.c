#include "../../library/plibrary.h"

int main() {
    setlocale(LC_NUMERIC, "");

    uint64_t ans = 0;

    FILE * file = fopen("names.txt", "r");
    if(file == NULL) {
        fprintf(stderr, "Unable to open file: \"names.txt\" for reading!\n");
        exit(EXIT_FAILURE);
    }

    char * curr_name = malloc(32);
    memset(curr_name, 0, 32);

    uint64_t start = ns();

    int name_index = 0;

    while(fgets(curr_name, 32, file) != NULL) {
        int score = 0;
        int i = 0;
        while(curr_name[i] != '\0') {
            if(curr_name[i] >= 'A')
                score += (curr_name[i] - 'A' + 1);
            i++;
        }
        score *= ++name_index;
        ans += score;
    }


    uint64_t end = ns();

    printf("Answer: %'lu\n", ans);

    char * timestamp = format_time(end - start);
    printf("Time elapsed: %s\n", timestamp);
    free(timestamp);

    free(curr_name);

    return 0;
}
