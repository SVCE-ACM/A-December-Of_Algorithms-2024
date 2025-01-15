from datetime import datetime, timedelta

class AlertManager:
    def __init__(self):
        self.alerts = {}

    def parse_timestamp(self, timestamp):
        try:
            return datetime.strptime(timestamp, "%H:%M:%S")
        except ValueError:
            raise ValueError(f"Invalid timestamp format: {timestamp}. Expected HH:MM:SS.")

    def process_alert(self, alert):
        alert_id = alert["id"]
        timestamp = self.parse_timestamp(alert["timestamp"])
        threat_level = alert["threat_level"]

        if alert_id in self.alerts:
            stored_alert = self.alerts[alert_id]
            stored_time = stored_alert["timestamp"]

            # Ignore alert if it's within 30 seconds
            if timestamp - stored_time <= timedelta(seconds=30):
                return

            # Update threat level if higher
            if threat_level > stored_alert["threat_level"]:
                self.alerts[alert_id]["threat_level"] = threat_level
                self.alerts[alert_id]["timestamp"] = timestamp
        else:
            self.alerts[alert_id] = {"timestamp": timestamp, "threat_level": threat_level}

    def evict_old_alerts(self, current_time):
        current_time = self.parse_timestamp(current_time)
        ids_to_remove = []

        print("\n[DEBUG] Current Time:", current_time)
        print("[DEBUG] Stored Alerts Before Eviction:")
        for alert_id, data in self.alerts.items():
            print(f"  - ID: {alert_id}, Timestamp: {data['timestamp']}, Threat Level: {data['threat_level']}")

        for alert_id, data in self.alerts.items():
            if current_time - data["timestamp"] > timedelta(minutes=5):
                print(f"[DEBUG] Evicting Alert ID: {alert_id} (Timestamp: {data['timestamp']})")
                ids_to_remove.append(alert_id)

        for alert_id in ids_to_remove:
            del self.alerts[alert_id]

        print("[DEBUG] Stored Alerts After Eviction:")
        for alert_id, data in self.alerts.items():
            print(f"  - ID: {alert_id}, Timestamp: {data['timestamp']}, Threat Level: {data['threat_level']}")

    def get_stored_alerts(self):
        result = []
        for alert_id, data in self.alerts.items():
            result.append({
                "id": alert_id,
                "timestamp": data["timestamp"].strftime("%H:%M:%S"),
                "threat_level": data["threat_level"]
            })
        return result


def main():
    alert_manager = AlertManager()
    print("Enter alerts in the format: id,timestamp,threat_level (e.g., A123,00:00:10,3)")
    print("Type 'stop' to finish...")

    while True:
        user_input = input("Enter alert: ").strip()
        if user_input.lower() == "stop":
            break

        try:
            alert_id, timestamp, threat_level = user_input.split(",")
            alert = {
                "id": alert_id.strip(),
                "timestamp": timestamp.strip(),
                "threat_level": int(threat_level.strip())
            }
            alert_manager.process_alert(alert)
        except ValueError as e:
            print(f"Invalid format. Please try again. Error: {e}")

    current_time = input("Enter the current time (HH:MM:SS): ").strip()
    try:
        alert_manager.evict_old_alerts(current_time)
    except ValueError as e:
        print(f"Error with current time: {e}")
        return

    print("\nStored alerts:")
    stored_alerts = alert_manager.get_stored_alerts()
    if not stored_alerts:
        print("No alerts to display.")
    else:
        for alert in stored_alerts:
            print(f"ID: {alert['id']}, Timestamp: {alert['timestamp']}, Threat Level: {alert['threat_level']}")


if __name__ == "__main__":
    main()

