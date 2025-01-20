import java.time.LocalDateTime
import java.time.temporal.ChronoUnit

data class AlertData(var timestamp: LocalDateTime?, var threatLevel: Int)

class AlertManager {
    private val alerts = mutableMapOf<String, AlertData>()
    private val lastSeen = mutableMapOf<String, LocalDateTime?>()

    fun processAlert(alert: Map<String, Any>) {
        val alertId = alert["id"] as String
        val currentTime = LocalDateTime.now()

        // Check for duplicates within 30 seconds
        if (lastSeen[alertId] != null && ChronoUnit.SECONDS.between(lastSeen[alertId], currentTime) < 30) {
            return
        }

        // Update alert information
        alerts[alertId]?.let {
            it.timestamp = currentTime
            it.threatLevel = maxOf(it.threatLevel, alert["threat_level"] as Int)
        } ?: run {
            alerts[alertId] = AlertData(currentTime, alert["threat_level"] as Int)
        }
        lastSeen[alertId] = currentTime
    }

    fun getAlerts(): List<AlertData> {
        val currentTime = LocalDateTime.now()
        return alerts.values.filter {
            ChronoUnit.MINUTES.between(it.timestamp, currentTime) < 5
        }
    }
}

fun main() {
    val alertManager = AlertManager()

    val alerts = listOf(
        mapOf("id" to "A123", "timestamp" to "00:00:10", "threat_level" to 3),
        mapOf("id" to "A123", "timestamp" to "00:00:15", "threat_level" to 3),
        mapOf("id" to "B456", "timestamp" to "00:00:20", "threat_level" to 2),
        mapOf("id" to "A123", "timestamp" to "00:00:30", "threat_level" to 5),
        mapOf("id" to "B456", "timestamp" to "00:05:05", "threat_level" to 2)
    )

    alerts.forEach { alertManager.processAlert(it) }

    val storedAlerts = alertManager.getAlerts()
    println(storedAlerts)
}
