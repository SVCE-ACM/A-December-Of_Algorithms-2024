import heapq

class TaskScheduler:
    def __init__(self):
        self.tasks_heap = []
        self.task_map = {}
        self.counter = 0

    def add_task(self, description, priority):
        task = (-priority, self.counter, description)
        heapq.heappush(self.tasks_heap, task)
        self.task_map[description] = task
        self.counter += 1
        print(f"Task '{description}' with priority {priority} added.")

    def remove_task(self, description):
        if description in self.task_map:
            task = self.task_map.pop(description)
            self.tasks_heap = [t for t in self.tasks_heap if t != task]
            heapq.heapify(self.tasks_heap)
            print(f"Task '{description}' removed.")
        else:
            print(f"Task '{description}' not found.")

    def search_task(self, description):
        if description in self.task_map:
            task = self.task_map[description]
            print(f"Task found: {task[2]} with priority {-task[0]}")
        else:
            print(f"Task '{description}' not found.")

    def display_tasks(self):
        sorted_tasks = sorted(self.tasks_heap, key=lambda x: x[0])
        print("Tasks in priority order:")
        for task in sorted_tasks:
            print(f"Task: {task[2]}, Priority: {-task[0]}")

def menu():
    scheduler = TaskScheduler()
    
    while True:
        print("\nTask Scheduler Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Search Task")
        print("4. Display Tasks")
        print("5. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            description = input("Enter task description: ")
            priority = int(input("Enter task priority: "))
            scheduler.add_task(description, priority)
            
        elif choice == 2:
            description = input("Enter task description to remove: ")
            scheduler.remove_task(description)
            
        elif choice == 3:
            description = input("Enter task description to search: ")
            scheduler.search_task(description)
            
        elif choice == 4:
            scheduler.display_tasks()
            
        elif choice == 5:
            print("Exiting Task Scheduler.")
            break
            
        else:
            print("Invalid choice. Please try again.")

menu()
