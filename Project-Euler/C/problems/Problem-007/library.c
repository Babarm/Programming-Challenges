#include "library.h"

// The following 2 methods are REQUIRED by every challenge
// Do not alter.
// Place new methods at EOF

// ===============================================================================================================================

// Nanosecond Timer
uint64_t ns() {
    static uint64_t is_init = 0;

    // APPLE
#if defined (__APPLE__)
    mach_timebase_info_data_t info;
    if(is_init == 0) {
        mach_timebase_info(&info);
        is_init = 1;
    }
    uint64_t now;
    now = mach_absolute_time();
    now *= info.numer;
    now /= info.denom;
    return now;

    // LINUX
#elif defined (__linux)
    struct timespec linux_rate;
    if(is_init == 0) {
        clock_getres(CLOCK_ID, &linux_rate);
        is_init = 1;
    }
    uint64_t now;
    struct timespec spec;
    clock_gettime(CLOCK_ID, &spec);
    now = spec.tv_sec * 1.0e9 + spec.tv_nsec;
    return now;

    // WINDOWS
#elif defined(_WIN32)
    LARGE_INTEGER win_frequency;
    if(is_init == 0) {
        QueryPerformanceFrequency(&win_frequency);
        is_init = 1;
    }
    LARGE_INTEGER now;
    QueryPerformanceCounter(&now);
    return (uint64_t) ((1e9 * now.QuadPart) / win_frequency.QuadPart);
#endif
}


// Timestamp Formatter
char * format_time(uint64_t span) {
    char * dest = malloc(32);
    // 1 sec <= span < inf
    if(span >= 1e9) sprintf(dest, "%.3f sec", (double)span / 1e9);
    
    // 1 ms <= span < 1000 ms
    else if(span >= 1e6) sprintf(dest, "%.3f ms", (double)span / 1e6);

    // 1 us <= span < 1000 us
    else if(span >= 1e3) sprintf(dest, "%.3f \u03BCs", (double)span / 1e3);

    // 1 ns <= span < 1000 ns
    else sprintf(dest, "%lu ns", span);

    return dest;
}

// ===============================================================================================================================

// Place New Methods Below
int is_prime(int n) {
    if(n == 2)
        return true;
    if(n < 2 || n % 2 == 0)
        return false;
    for(int i = 3; i * i <= n; i += 2)
        if(n % i == 0)
            return false;
    return true;
}
