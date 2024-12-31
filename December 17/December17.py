from datetime import datetime
import json
class AlertManager:
    def __init__(self):
        self.alerts = {}

    def parse_time(self, time_str):
        return datetime.strptime(time_str, "%H:%M:%S")

    def process_alert(self, alert):
        alert_id = alert["id"]
        timestamp = self.parse_time(alert["timestamp"])
        threat_level = alert["threat_level"]

        current_time = timestamp
        for key in list(self.alerts.keys()):
            if (current_time - self.alerts[key]["timestamp"]).total_seconds() > 300:
                del self.alerts[key]

        if alert_id in self.alerts:
            existing_alert = self.alerts[alert_id]
            if (timestamp - existing_alert["timestamp"]).total_seconds() <= 30:
                if threat_level > existing_alert["threat_level"]:
                    self.alerts[alert_id]["timestamp"] = timestamp
                    self.alerts[alert_id]["threat_level"] = threat_level
                return

        self.alerts[alert_id] = {
            "timestamp": timestamp,
            "threat_level": threat_level
        }

    def get_stored_alerts(self):
        return [
            {
                "id": alert_id,
                "timestamp": alert["timestamp"].strftime("%H:%M:%S"),
                "threat_level": alert["threat_level"]
            }
            for alert_id, alert in self.alerts.items()
        ]

alerts = json.loads(input())

manager1 = AlertManager()
for alert in alerts:
    manager1.process_alert(alert)

print("Stored alerts:")
print(manager1.get_stored_alerts())