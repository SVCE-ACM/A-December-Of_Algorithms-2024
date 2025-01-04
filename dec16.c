//(16) Train Platform Calculation
#include <stdio.h>
#include <stdlib.h>

int minPlatforms(int arrivals[], int departures[], int N) {
    int platforms = 0, result = 0;
    int i = 0, j = 0;
    while (i < N && j < N) {
        if (arrivals[i] <= departures[j]) {
            platforms++;
            i++;
        } else {
            platforms--;
            j++;
        }
        if (platforms > result) result = platforms;
    }
    return result;
}

int main() {
    int arrivals[] = {900, 940, 950, 1100, 1500, 1800};
    int departures[] = {910, 1200, 1120, 1130, 1900, 2000};
    int N = sizeof(arrivals) / sizeof(arrivals[0]);
    printf("Minimum platforms required: %d\n", minPlatforms(arrivals, departures, N));
    return 0;
}

