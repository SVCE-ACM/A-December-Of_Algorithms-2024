//(15) Holiday Gift Arrangement
#include <stdio.h>
#include <stdlib.h>

int minTrips(int houses[], int N, int W) {
    int trips = 0, current_load = 0;
    for (int i = 0; i < N; i++) {
        if (current_load + houses[i] <= W) {
            current_load += houses[i];
        } else {
            trips++;
            current_load = houses[i];
        }
    }
    if (current_load > 0) trips++;
    return trips;
}

int main() {
    int houses[] = {2, 3, 5, 2, 1};
    int W = 6;
    int N = sizeof(houses) / sizeof(houses[0]);
    printf("%d\n", minTrips(houses, N, W));
    return 0;
}

