#include "plibrary.h"

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


// Reverses an integer
int reverse_int(int n) {
    int reverse = 0;
    do {
        reverse *= 10;
        reverse += n % 10;
        n /= 10;
    } while(n > 0);
    return reverse;
}


// Determines if an int is a palindrome
int is_palindrome_int(int n) {
    return n == reverse_int(n);
}


// Determines if a number is prime
int is_prime(int n) {
    if(n == 2) return true;
    if(n < 2 || n % 2 == 0) return false;
    for(int i = 3; i * i <= n; i += 2) if(n % i == 0) return false;
    return true;
}


// Generates a list of prime numbers below a given limit
int * prime_sieve(int limit) {
    if(limit < 2)
        return NULL;

    char * is_prime = malloc(limit + 1);
    memset(is_prime, true, limit + 1);
    is_prime[0] = is_prime[1] = false;

    for(int i = 2; i * i <= limit; i++) {
        if(is_prime[i]) {
            for(int j = i * i; j <= limit; j += i) {
                is_prime[j] = false;
            }
        }
    }

    int num_primes = 0;
    for(int i = 2; i <= limit; i++) {
        if(is_prime[i]) {
            num_primes++;
        }
    }

    int * primes = malloc(sizeof(int) * (num_primes + 1));
    int k = 0;
    for(int i = 2; i <= limit; i++) {
        if(is_prime[i]) {
            primes[k++] = i;
        }
    }

    primes[num_primes] = 0;

    free(is_prime);
    return primes;
}


// Determines the larger of two numbers
int max(int a, int b) {
    return a > b ? a : b;
}

// Counts the number of divisors of a number
int num_divisors(int n) {
    int limit = n;
    int count = 0;
    if(n == 1) return 1;
    for(int i = 1; i < limit; ++i) {
        if(n % i == 0) {
            limit = n / i;
            if(limit != i) {
                count++;
            }
            count++;
        }
    }
    return count;
}


// Determines the factorial of a number
double factorial(int n) {
    double result = 1.0F;
    for(int i = 2; i <= n; i++)
        result *= i;
    return result;
}

// Number of combinations (n choose k)
uint64_t C(int n, int k) {
    return (uint64_t) (factorial(n) / (factorial(n - k) * factorial(k)));
}


// Calculates n to the power of k
double pow(double n, double k) {
    if(n == 0) return 0.0;
    if(k == 0) return 1.0;
    double prod = 1.0;
    for(int i = n; i < k; i++) {
        prod *= n;
    }
    return prod;
}


const char * digit_reps[] = { "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen" };

const char * tens_reps[] = { "", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety" };

// Converts an arabic number to its english representation
char * num2string(int n) {
    char * string = malloc(128);
    memset(string, 0, 128);

    if(n > 9999 || n < 0) return string;

    if(n == 0) strcpy(string, digit_reps[0]);

    int val;

    while(n != 0) {
        if(n >= 1000) {
            val = n / 1000;
            n %= 1000;
            strcpy(string + strlen(string), digit_reps[val]);
            strcpy(string + strlen(string), " thousand");
            if(n > 0)
                string[strlen(string)] = ' ';
        }
        if(n >= 100) {
            val = n / 100;
            n %= 100;
            strcpy(string + strlen(string), digit_reps[val]);
            strcpy(string + strlen(string), " hundred");
            if(n > 0)
                strcpy(string + strlen(string), " and ");
        }
        if(n >= 20) {
            val = n / 10;
            n %= 10;
            strcpy(string + strlen(string), tens_reps[val]);
            if(n > 0)
                string[strlen(string)] = ' ';
        }
        if(n > 0) {
            strcpy(string + strlen(string), digit_reps[n]);
            n = 0;
        }
    }

    return string;
}


// Determines the sum of the proper divisors of a number
int sum_divisors(int n) {
    if(n == 0) return 0;
    int sum = 1;
    for(int i = 2; i < n; i++) {
        if(n % i == 0)
            sum += i;
    }
    return sum;
}
