#include "../../library/plibrary.h"

#define MAX 6000

int main() {
    setlocale(LC_NUMERIC, "");

    uint64_t ans = 0;

    FILE * file = fopen("names.txt", "r");
    if(file == NULL) {
        fprintf(stderr, "Unable to open file: \"names.txt\" for reading!\n");
        exit(EXIT_FAILURE);
    }

    char ** names = malloc(sizeof(char *) * MAX);
    for(int i = 0; i < MAX; i++) {
        names[i] = malloc(32);
        memset(names[i], 0, 32);
    }


    uint64_t start = ns();

    int name_index = 0;
    while(fgets(names[name_index++], 32, file) != NULL);

    uint64_t end = ns();

    printf("Answer: %'lu\n", ans);

    char * timestamp = format_time(end - start);
    printf("Time elapsed: %s\n", timestamp);
    free(timestamp);

    for(int i = 0; i < MAX; i++) {
        free(names[i]);
    }
    free(names);

    return 0;
}
