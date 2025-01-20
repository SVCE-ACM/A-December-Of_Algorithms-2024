#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int minPlatforms(vector<int>& arrivals, vector<int>& departures) {
    sort(arrivals.begin(), arrivals.end());
    sort(departures.begin(), departures.end());

    int platformsNeeded = 0, currentPlatforms = 0;
    int i = 0, j = 0;

    while (i < arrivals.size()) {
        if (arrivals[i] <= departures[j]) {
            currentPlatforms++;
            i++;
        } else {
            currentPlatforms--;
            j++;
        }
        platformsNeeded = max(platformsNeeded, currentPlatforms);
    }
    return platformsNeeded;
}
