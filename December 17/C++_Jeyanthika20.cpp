#include <iostream>
#include <map>
#include <vector>
using namespace std;

struct Alert {
    int timestamp;
    int threatLevel;
};

class AlertManager {
    map<string, Alert> alerts;

public:
    void processAlert(string id, int timestamp, int threatLevel) {
        if (alerts.count(id) && timestamp - alerts[id].timestamp < 30) return;

        alerts[id].timestamp = timestamp;
        alerts[id].threatLevel = max(alerts[id].threatLevel, threatLevel);
    }

    vector<Alert> getAlerts(int currentTime) {
        vector<Alert> validAlerts;
        for (auto& entry : alerts) {
            if (currentTime - entry.second.timestamp < 300) {
                validAlerts.push_back(entry.second);
            }
        }
        return validAlerts;
    }
};
