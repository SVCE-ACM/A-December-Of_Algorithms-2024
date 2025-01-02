from collections import defaultdict
from datetime import datetime, timedelta

class AlertManager:
    def _init_(self):
        self.alerts = defaultdict(lambda: {"timestamp": None, "threat_level": 0})
        self.last_seen = defaultdict(lambda: None)

    def process_alert(self, alert):
        alert_id = alert["id"]
        current_time = datetime.now()

        # Check for duplicates within 30 seconds
        if self.last_seen[alert_id] and (current_time - self.last_seen[alert_id]) < timedelta(seconds=30):
            return

        # Update alert information
        self.alerts[alert_id]["timestamp"] = current_time
        self.alerts[alert_id]["threat_level"] = max(self.alerts[alert_id]["threat_level"], alert["threat_level"])
        self.last_seen[alert_id] = current_time

    def get_alerts(self):
        current_time = datetime.now()
        valid_alerts = []
        for alert_id, alert_data in self.alerts.items():
            if (current_time - alert_data["timestamp"]) < timedelta(minutes=5):
                valid_alerts.append(alert_data)
        return valid_alerts

alert_manager = AlertManager()

alerts = [
    {"id": "A123", "timestamp": "00:00:10", "threat_level": 3},
    {"id": "A123", "timestamp": "00:00:15", "threat_level": 3},
    {"id": "B456", "timestamp": "00:00:20", "threat_level": 2},
    {"id": "A123", "timestamp": "00:00:30", "threat_level": 5},
    {"id": "B456", "timestamp": "00:05:05", "threat_level": 2}
]
for alert in alerts:
    alert_manager.process_alert(alert)

stored_alerts = alert_manager.get_alerts()
print(stored_alerts)
