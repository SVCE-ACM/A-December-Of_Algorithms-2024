import time

alerts = {}

def process_alerts(incoming_alerts):
    current_time = time.time()
    result = []

    for alert in incoming_alerts:
        alert_id = alert["id"]
        alert_timestamp = time.strptime(alert["timestamp"], "%H:%M:%S")
        alert_time_in_sec = time.mktime(alert_timestamp)
        alert_threat_level = alert["threat_level"]

        remove_old_alerts(current_time)

        if alert_id in alerts:
            last_alert_time, last_threat_level = alerts[alert_id]

            if current_time - last_alert_time <= 30:
                continue

            if alert_threat_level > last_threat_level:
                alerts[alert_id] = (alert_time_in_sec, alert_threat_level)
        else:
            alerts[alert_id] = (alert_time_in_sec, alert_threat_level)

    for alert_id, (timestamp, threat_level) in alerts.items():
        alert_timestamp = time.strftime("%H:%M:%S", time.localtime(timestamp))
        result.append({"id": alert_id, "timestamp": alert_timestamp, "threat_level": threat_level})

    return result

def remove_old_alerts(current_time):
    to_remove = []
    for alert_id, (timestamp, _) in alerts.items():
        if current_time - timestamp > 5 * 60:
            to_remove.append(alert_id)
    for alert_id in to_remove:
        del alerts[alert_id]

incoming_alerts_1 = [
    {"id": "A123", "timestamp": "00:00:10", "threat_level": 3},
    {"id": "A123", "timestamp": "00:00:15", "threat_level": 3},
    {"id": "B456", "timestamp": "00:00:20", "threat_level": 2},
    {"id": "A123", "timestamp": "00:00:30", "threat_level": 5},
    {"id": "B456", "timestamp": "00:05:05", "threat_level": 2}
]
result_1 = process_alerts(incoming_alerts_1)
print("Stored alerts (Output 1):", result_1)

incoming_alerts_2 = [
    {"id": "X001", "timestamp": "12:00:00", "threat_level": 1},
    {"id": "Y002", "timestamp": "12:02:30", "threat_level": 3},
    {"id": "X001", "timestamp": "12:02:45", "threat_level": 2},
    {"id": "Z003", "timestamp": "12:07:00", "threat_level": 4}
]
result_2 = process_alerts(incoming_alerts_2)
print("Stored alerts (Output 2):", result_2)
