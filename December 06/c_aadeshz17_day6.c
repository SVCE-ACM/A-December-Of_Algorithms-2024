#include <stdio.h> 
 #include <string.h> 
 #include <stdlib.h> 
 #define MAX_TASKS 100 
 typedef struct Task { 
     char task_id[100]; 
     char dependencies[MAX_TASKS][100]; 
     int dep_count;  
 } Task; 
 int find_task_index(Task tasks[], int num_tasks, char *task_id) { 
     for (int i = 0; i < num_tasks; i++) { 
         if (strcmp(tasks[i].task_id, task_id) == 0) { 
             return i; 
         } 
     } 
     return -1; 
 } 
 int topological_sort(Task tasks[], int num_tasks, char result[MAX_TASKS][100]) { 
     int in_degree[MAX_TASKS] = {0};   
     int queue[MAX_TASKS], front = 0, rear = 0; 
     for (int i = 0; i < num_tasks; i++) { 
         for (int j = 0; j < tasks[i].dep_count; j++) { 
             int dep_index = find_task_index(tasks, num_tasks, tasks[i].dependencies[j]); 
             if (dep_index != -1) { 
                 in_degree[dep_index]++; 
             } 
         } 
     } 
     for (int i = 0; i < num_tasks; i++) { 
         if (in_degree[i] == 0) { 
             queue[rear++] = i; 
         } 
     } 
     int task_count = 0; 
     while (front < rear) { 
         int level_size = rear - front; 
         char level[MAX_TASKS][100];   
         int level_count = 0; 
         for (int i = 0; i < level_size; i++) { 
             int task_index = queue[front++]; 
             strcpy(level[level_count++], tasks[task_index].task_id); 
             for (int j = 0; j < tasks[task_index].dep_count; j++) { 
                 int dep_index = find_task_index(tasks, num_tasks, tasks[task_index].dependencies[j]); 
                 if (dep_index != -1) { 
                     in_degree[dep_index]--; 
                     if (in_degree[dep_index] == 0) { 
                         queue[rear++] = dep_index; 
                     } 
                 } 
             } 
         } 
         for (int i = 0; i < level_count; i++) { 
             strcpy(result[task_count++], level[i]); 
         } 
     }    if (task_count == num_tasks) { 
         return 1;   
     } else { 
         return 0;  
     } 
 } 
 int main() { 
     int num_tasks; 
     printf("Enter number of tasks: "); 
     scanf("%d", &num_tasks); 
     Task tasks[MAX_TASKS]; 
     char result[MAX_TASKS][100]; 
     for (int i = 0; i < num_tasks; i++) { 
         printf("Enter task id: "); 
         scanf("%s", tasks[i].task_id); 
         printf("Enter dependencies (enter 'done' to finish): "); 
         tasks[i].dep_count = 0; 
         while (1) { 
             char dep[100]; 
             scanf("%s", dep); 
             if (strcmp(dep, "done") == 0) { 
                 break; 
             } 
             strcpy(tasks[i].dependencies[tasks[i].dep_count++], dep); 
         } 
     } 
     if (topological_sort(tasks, num_tasks, result)) { 
         printf("Task execution order (concurrent steps):\n"); 
         for (int i = 0; i < num_tasks; i++) { 
             printf("[%s]\n", result[i]); 
         } 
     } else { 
         printf("Error: Cyclic dependency detected\n"); 
     } 
     return 0; 
 } 
 