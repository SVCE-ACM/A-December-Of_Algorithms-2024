using System;
using System.Collections.Generic;
using System.Linq;

class AlertManager
{
    private Dictionary<string, (DateTime timestamp, int threatLevel)> alerts;
    private Dictionary<string, DateTime?> lastSeen;

    public AlertManager()
    {
        alerts = new Dictionary<string, (DateTime, int)>();
        lastSeen = new Dictionary<string, DateTime?>();
    }

    public void ProcessAlert(Dictionary<string, object> alert)
    {
        string alertId = alert["id"].ToString();
        DateTime currentTime = DateTime.Now;

        // Check for duplicates within 30 seconds
        if (lastSeen.ContainsKey(alertId) && lastSeen[alertId].HasValue && (currentTime - lastSeen[alertId].Value).TotalSeconds < 30)
        {
            return;
        }

        // Update alert information
        if (alerts.ContainsKey(alertId))
        {
            int existingThreatLevel = alerts[alertId].threatLevel;
            alerts[alertId] = (currentTime, Math.Max(existingThreatLevel, Convert.ToInt32(alert["threat_level"])));
        }
        else
        {
            alerts[alertId] = (currentTime, Convert.ToInt32(alert["threat_level"]));
        }

        lastSeen[alertId] = currentTime;
    }

    public List<(DateTime timestamp, int threatLevel)> GetAlerts()
    {
        DateTime currentTime = DateTime.Now;
        var validAlerts = new List<(DateTime timestamp, int threatLevel)>();

        foreach (var alert in alerts)
        {
            if ((currentTime - alert.Value.timestamp).TotalMinutes < 5)
            {
                validAlerts.Add(alert.Value);
            }
        }

        return validAlerts;
    }
}

class Program
{
    static void Main()
    {
        var alertManager = new AlertManager();

        var alerts = new List<Dictionary<string, object>>()
        {
            new Dictionary<string, object> { { "id", "A123" }, { "timestamp", "00:00:10" }, { "threat_level", 3 } },
            new Dictionary<string, object> { { "id", "A123" }, { "timestamp", "00:00:15" }, { "threat_level", 3 } },
            new Dictionary<string, object> { { "id", "B456" }, { "timestamp", "00:00:20" }, { "threat_level", 2 } },
            new Dictionary<string, object> { { "id", "A123" }, { "timestamp", "00:00:30" }, { "threat_level", 5 } },
            new Dictionary<string, object> { { "id", "B456" }, { "timestamp", "00:05:05" }, { "threat_level", 2 } }
        };

        foreach (var alert in alerts)
        {
            alertManager.ProcessAlert(alert);
        }

        var storedAlerts = alertManager.GetAlerts();
        foreach (var alert in storedAlerts)
        {
            Console.WriteLine($"Timestamp: {alert.timestamp}, Threat Level: {alert.threatLevel}");
        }
    }
}
