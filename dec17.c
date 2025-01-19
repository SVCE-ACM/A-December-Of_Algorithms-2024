//(17) Cybersecurity Alert Management:
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define MAX_ALERTS 1000
#define TIME_WINDOW 30
#define EVICTION_TIME 300

typedef struct {
    char id[10];
    int threat_level;
    time_t timestamp;
} Alert;

typedef struct {
    Alert alerts[MAX_ALERTS];
    int count;
} AlertTable;

time_t parse_timestamp(char* timestamp) {
    struct tm tm;
    strptime(timestamp, "%H:%M:%S", &tm);
    return mktime(&tm);
}

int find_alert(AlertTable* table, const char* id) {
    for (int i = 0; i < table->count; i++) {
        if (strcmp(table->alerts[i].id, id) == 0) {
            return i;
        }
    }
    return -1;
}

void evict_old_alerts(AlertTable* table, time_t current_time) {
    for (int i = 0; i < table->count; i++) {
        if (difftime(current_time, table->alerts[i].timestamp) > EVICTION_TIME) {
            for (int j = i; j < table->count - 1; j++) {
                table->alerts[j] = table->alerts[j + 1];
            }
            table->count--;
            i--;
        }
    }
}

void process_alert(AlertTable* table, const char* id, time_t timestamp, int threat_level) {
    evict_old_alerts(table, timestamp);
    int index = find_alert(table, id);
    if (index == -1) {
        if (table->count < MAX_ALERTS) {
            Alert alert;
            strcpy(alert.id, id);
            alert.timestamp = timestamp;
            alert.threat_level = threat_level;
            table->alerts[table->count++] = alert;
        }
    } else {
        if (difftime(timestamp, table->alerts[index].timestamp) > TIME_WINDOW) {
            table->alerts[index].timestamp = timestamp;
            table->alerts[index].threat_level = threat_level;
        }
    }
}

void print_alerts(AlertTable* table) {
    for (int i = 0; i < table->count; i++) {
        printf("{\"id\": \"%s\", \"timestamp\": \"%02ld:%02ld:%02ld\", \"threat_level\": %d}\n", 
                table->alerts[i].id, 
                table->alerts[i].timestamp / 3600, 
                (table->alerts[i].timestamp % 3600) / 60, 
                table->alerts[i].timestamp % 60, 
                table->alerts[i].threat_level);
    }
}

int main() {
    AlertTable table = {0};
    char* incoming_alerts[][3] = {
        {"A123", "00:00:10", "3"},
        {"A123", "00:00:15", "3"},
        {"B456", "00:00:20", "2"},
        {"A123", "00:00:30", "5"},
        {"B456", "00:05:05", "2"}
    };
    int n = 5;
    for (int i = 0; i < n; i++) {
        time_t timestamp = parse_timestamp(incoming_alerts[i][1]);
        int threat_level = atoi(incoming_alerts[i][2]);
        process_alert(&table, incoming_alerts[i][0], timestamp, threat_level);
    }
    printf("Stored alerts:\n");
    print_alerts(&table);
    return 0;
}

