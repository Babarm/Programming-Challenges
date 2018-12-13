/*
   Kevin Conte
   Dec 2018
   ===========
   Problem 1: Multiples of 3 and 5
   ===============================
*/

#include <stdio.h>

int main() {
    int ans = 0;

    // First sum all numbers divisible by 3
    // To do so, find the 333th triangle number (all numbers from 1 to 333 summed) and multiply by 3
    int p = 999 / 3;
    ans += 3 * (p * (p + 1)) / 2;

    // Add the sum of all numbers divisible by 5
    // Using the same method as above, with 3 substituted with 5
    p = 999 / 5;
    ans += 5 * (p * (p + 1)) / 2;

    // Finally, remove all numbers divisible by 15 to avoid double counting.
    // Using the same method as above, with 3 substituted with 15
    p = 999 / 15;
    ans -= 15 * (p * (p + 1)) / 2;

    printf("%d\n", ans);

    return 0;
}
