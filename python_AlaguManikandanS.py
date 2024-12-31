import bisect
import json

class TaskScheduler:
    def __init__(self, storage_file="tasks.json"):
        self.tasks = []
        self.task_map = {}
        self.storage_file = storage_file
        self.load_tasks()

    def add_task(self, task_name, priority):
        if task_name in self.task_map:
            print("Task already exists.")
            return
        bisect.insort(self.tasks, (-priority, task_name))
        self.task_map[task_name] = priority
        self.save_tasks()

    def remove_task(self, task_name):
        if task_name not in self.task_map:
            print("Task not found.")
            return
        priority = self.task_map.pop(task_name)
        self.tasks.remove((-priority, task_name))
        self.save_tasks()

    def search_task(self, task_name):
        return self.task_map.get(task_name, None)

    def display_tasks(self):
        return [(task[1], -task[0]) for task in self.tasks]

    def save_tasks(self):
        with open(self.storage_file, "w") as f:
            json.dump({"tasks": self.tasks, "task_map": self.task_map}, f)

    def load_tasks(self):
        try:
            with open(self.storage_file, "r") as f:
                data = json.load(f)
                self.tasks = data["tasks"]
                self.task_map = data["task_map"]
        except FileNotFoundError:
            pass

def menu():
    scheduler = TaskScheduler()
    while True:
        print("\nTask Scheduler Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Search Task")
        print("4. Display Tasks")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            task_name = input("Enter task name: ")
            priority = int(input("Enter task priority (higher number = higher priority): "))
            scheduler.add_task(task_name, priority)
        elif choice == "2":
            task_name = input("Enter task name to remove: ")
            scheduler.remove_task(task_name)
        elif choice == "3":
            task_name = input("Enter task name to search: ")
            priority = scheduler.search_task(task_name)
            if priority is not None:
                print(f"Task found: {task_name} with priority {priority}")
            else:
                print("Task not found.")
        elif choice == "4":
            tasks = scheduler.display_tasks()
            print("Tasks in priority order:", tasks)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
