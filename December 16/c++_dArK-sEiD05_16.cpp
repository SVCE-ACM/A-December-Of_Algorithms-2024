#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int min_platforms(vector<int>& arrivals, vector<int>& departures) {
    sort(arrivals.begin(), arrivals.end());
    sort(departures.begin(), departures.end());

    int platforms_needed = 0;
    int current_platforms = 0;

    int i = 0, j = 0;

    while (i < arrivals.size()) {
        if (arrivals[i] <= departures[j]) {
            current_platforms++;
            i++;
        } else {
            current_platforms--;
            j++;
        }

        platforms_needed = max(platforms_needed, current_platforms);
    }

    return platforms_needed;
}

int main() {
    vector<int> arrivals = {100, 180, 270, 320, 450};
    vector<int> departures = {200, 250, 350, 400, 500};

    cout << "Minimum platforms required: " << min_platforms(arrivals, departures) << endl;

    return 0;
}
