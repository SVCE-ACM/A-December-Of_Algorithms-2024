#include <iostream>
#include <unordered_map>
#include <deque>
#include <vector>
#include <string>
#include <chrono>
#include <queue>
#include <algorithm>

using namespace std;

class AlertManager {
private:
    struct Alert {
        chrono::system_clock::time_point timestamp;
        int threat_level;

        bool operator>(const Alert& other) const {
            return timestamp > other.timestamp;
        }
    };

    unordered_map<string, Alert> alerts;
    priority_queue<pair<chrono::system_clock::time_point, string>, vector<pair<chrono::system_clock::time_point, string>>, greater<>> alert_queue;
    unordered_map<string, chrono::system_clock::time_point> last_seen;
    chrono::minutes alert_expiry_time = chrono::minutes(5);
    chrono::seconds duplicate_time_limit = chrono::seconds(30);

    chrono::system_clock::time_point str_to_time(const string& timestamp) {
        int hours, minutes, seconds;
        sscanf(timestamp.c_str(), "%d:%d:%d", &hours, &minutes, &seconds);
        auto time = chrono::hours(hours) + chrono::minutes(minutes) + chrono::seconds(seconds);
        return chrono::system_clock::now() - time;
    }

public:
    void process_alert(const string& alert_id, const string& timestamp, int threat_level) {
        chrono::system_clock::time_point current_time = str_to_time(timestamp);

        if (last_seen.find(alert_id) != last_seen.end() &&
            chrono::duration_cast<chrono::seconds>(current_time - last_seen[alert_id]) < duplicate_time_limit) {
            return; // Skip duplicate alert
        }

        if (alerts.find(alert_id) == alerts.end() || current_time > alerts[alert_id].timestamp) {
            alerts[alert_id] = {current_time, threat_level};
            alert_queue.push({current_time, alert_id});
        }

        last_seen[alert_id] = current_time;
    }

    vector<pair<string, pair<string, int>>> get_alerts() {
        chrono::system_clock::time_point current_time = chrono::system_clock::now();
        vector<pair<string, pair<string, int>>> valid_alerts;

        while (!alert_queue.empty() &&
               chrono::duration_cast<chrono::minutes>(current_time - alert_queue.top().first) > alert_expiry_time) {
            string expired_alert_id = alert_queue.top().second;
            alert_queue.pop();
            alerts.erase(expired_alert_id); // Remove expired alerts
        }

        for (const auto& alert : alerts) {
            const auto& alert_data = alert.second;
            if (chrono::duration_cast<chrono::minutes>(current_time - alert_data.timestamp) <= alert_expiry_time) {
                valid_alerts.push_back({alert.first, {"Timestamp: " + to_string(chrono::duration_cast<chrono::seconds>(alert_data.timestamp.time_since_epoch()).count()), alert_data.threat_level}});
            }
        }

        return valid_alerts;
    }
};

int main() {
    AlertManager alert_manager;

    vector<pair<string, pair<string, int>>> alerts = {
        {"A123", {"00:00:10", 3}},
        {"A123", {"00:00:15", 3}},
        {"B456", {"00:00:20", 2}},
        {"A123", {"00:00:30", 5}},
        {"B456", {"00:05:05", 2}}
    };

    for (const auto& alert : alerts) {
        alert_manager.process_alert(alert.first, alert.second.first, alert.second.second);
    }

    vector<pair<string, pair<string, int>>> stored_alerts = alert_manager.get_alerts();
    for (const auto& alert : stored_alerts) {
        cout << "Alert ID: " << alert.first << ", Timestamp: " << alert.second.first
             << ", Threat Level: " << alert.second.second << endl;
    }

    return 0;
}
