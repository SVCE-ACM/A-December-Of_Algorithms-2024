#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int earthquakePropagation(vector<vector<int>>& buildings) {
    int maxAffected = 0;

    for (int i = 0; i < buildings.size(); i++) {
        int affected = 1;
        for (int j = 0; j < buildings.size(); j++) {
            if (i != j) {
                double distance = sqrt(pow(buildings[i][0] - buildings[j][0], 2) +
                                       pow(buildings[i][1] - buildings[j][1], 2));
                if (distance <= buildings[i][2]) affected++;
            }
        }
        maxAffected = max(maxAffected, affected);
    }

    return maxAffected;
}
