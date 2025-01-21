#include <iostream>
#include <vector>
using namespace std;

int minTrips(vector<int>& houses, int W) {
    int trips = 0, currentLoad = 0;

    for (int gifts : houses) {
        if (currentLoad + gifts > W) {
            trips++;
            currentLoad = 0;
        }
        currentLoad += gifts;
    }

    if (currentLoad > 0) trips++;
    return trips;
}
