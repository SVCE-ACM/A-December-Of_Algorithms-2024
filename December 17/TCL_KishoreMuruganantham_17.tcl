package require dict

namespace eval AlertManager {
    proc init {} {
        return [dict create alerts {} last_seen {}]
    }

    proc process_alert {alert} {
        upvar 1 $::AlertManager alerts
        upvar 1 $::AlertManager last_seen
        
        set alert_id [dict get $alert id]
        set current_time [clock seconds]

        if {[dict exists $last_seen $alert_id]} {
            set last_time [dict get $last_seen $alert_id]
            if {[expr {$current_time - $last_time} < 30]} {
                return
            }
        }

        dict set $alerts $alert_id [dict create timestamp $current_time threat_level [dict get $alert threat_level]]
        dict set $last_seen $alert_id $current_time
    }

    proc get_alerts {} {
        upvar 1 $::AlertManager alerts
        upvar 1 $::AlertManager last_seen

        set current_time [clock seconds]
        set valid_alerts {}

        foreach {alert_id alert_data} [dict get $alerts] {
            set timestamp [dict get $alert_data timestamp]
            if {[expr {$current_time - $timestamp} < 300]} {
                lappend valid_alerts $alert_data
            }
        }

        return $valid_alerts
    }
}

set alert_manager [AlertManager::init]

set alerts {
    {id "A123" timestamp "00:00:10" threat_level 3}
    {id "A123" timestamp "00:00:15" threat_level 3}
    {id "B456" timestamp "00:00:20" threat_level 2}
    {id "A123" timestamp "00:00:30" threat_level 5}
    {id "B456" timestamp "00:05:05" threat_level 2}
}

foreach alert $alerts {
    AlertManager::process_alert $alert
}

set stored_alerts [AlertManager::get_alerts]
puts $stored_alerts
