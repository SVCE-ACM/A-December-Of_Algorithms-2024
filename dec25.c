//(25) Task Scheduler
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Task {
    char description[100];
    int priority;
    struct Task* next;
} Task;

Task* head = NULL;

Task* createTask(char* description, int priority) {
    Task* newTask = (Task*)malloc(sizeof(Task));
    strcpy(newTask->description, description);
    newTask->priority = priority;
    newTask->next = NULL;
    return newTask;
}

void addTask(char* description, int priority) {
    Task* newTask = createTask(description, priority);
    if (head == NULL || head->priority < priority) {
        newTask->next = head;
        head = newTask;
    } else {
        Task* temp = head;
        while (temp->next != NULL && temp->next->priority >= priority) {
            temp = temp->next;
        }
        newTask->next = temp->next;
        temp->next = newTask;
    }
}

void removeTask(char* description) {
    Task* temp = head;
    Task* prev = NULL;
    while (temp != NULL && strcmp(temp->description, description) != 0) {
        prev = temp;
        temp = temp->next;
    }
    if (temp == NULL) {
        printf("Task not found.\n");
        return;
    }
    if (prev == NULL) {
        head = temp->next;
    } else {
        prev->next = temp->next;
    }
    free(temp);
}

Task* searchTask(char* description) {
    Task* temp = head;
    while (temp != NULL) {
        if (strcmp(temp->description, description) == 0) {
            return temp;
        }
        temp = temp->next;
    }
    return NULL;
}

void displayTasks() {
    Task* temp = head;
    printf("Task List:\n");
    while (temp != NULL) {
        printf("Task: %s, Priority: %d\n", temp->description, temp->priority);
        temp = temp->next;
    }
}

void menu() {
    int choice;
    char description[100];
    int priority;
    
    while (1) {
        printf("\n1. Add Task\n2. Remove Task\n3. Search Task\n4. Display Tasks\n5. Exit\nEnter your choice: ");
        scanf("%d", &choice);
        getchar();  // to clear the newline character left by scanf
        
        switch (choice) {
            case 1:
                printf("Enter task description: ");
                fgets(description, 100, stdin);
                description[strcspn(description, "\n")] = '\0';
                printf("Enter priority: ");
                scanf("%d", &priority);
                addTask(description, priority);
                break;
            case 2:
                printf("Enter task description to remove: ");
                fgets(description, 100, stdin);
                description[strcspn(description, "\n")] = '\0';
                removeTask(description);
                break;
            case 3:
                printf("Enter task description to search: ");
                fgets(description, 100, stdin);
                description[strcspn(description, "\n")] = '\0';
                Task* task = searchTask(description);
                if (task) {
                    printf("Task found: %s, Priority: %d\n", task->description, task->priority);
                } else {
                    printf("Task not found.\n");
                }
                break;
            case 4:
                displayTasks();
                break;
            case 5:
                printf("Exiting...\n");
                return;
            default:
                printf("Invalid choice.\n");
        }
    }
}

int main() {
    menu();
    return 0;
}

