import heapq
import pickle

class TaskScheduler:
    def __init__(self):
        self.task_queue = [] 
        self.task_map = {}   

    def add_task(self, description, priority):
        if description in self.task_map:
            print(f"Task '{description}' already exists.")
            return
        task = (priority, description)
        heapq.heappush(self.task_queue, (-priority, description))  
        self.task_map[description] = task
        print(f"Added task: {description} with priority {priority}")

    def remove_task(self, description):
        if description not in self.task_map:
            print(f"Task '{description}' not found.")
            return
        del self.task_map[description]
        self.task_queue = [(-p, d) for p, d in self.task_map.values()]
        heapq.heapify(self.task_queue)
        print(f"Removed task: {description}")

    def search_task(self, description):
        if description in self.task_map:
            priority = self.task_map[description][0]
            print(f"Task found: {description} with priority {priority}")
        else:
            print(f"Task '{description}' not found.")

    def display_tasks(self):
        tasks = sorted(self.task_map.values(), key=lambda x: -x[0])
        print("Tasks in priority order:")
        for priority, description in tasks:
            print(f"Task: {description}, Priority: {priority}")

    def save_to_file(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.task_map, file)
        print("Tasks saved to file.")

    def load_from_file(self, filename):
        try:
            with open(filename, 'rb') as file:
                self.task_map = pickle.load(file)
            self.task_queue = [(-p, d) for p, d in self.task_map.values()]
            heapq.heapify(self.task_queue)
            print("Tasks loaded from file.")
        except FileNotFoundError:
            print("No existing file found. Starting with an empty scheduler.")

if __name__ == "__main__":
    scheduler = TaskScheduler()
    scheduler.load_from_file("tasks.pkl")

    while True:
        print("\nTask Scheduler Menu")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Search Task")
        print("4. Display Tasks")
        print("5. Save and Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            desc = input("Enter task description: ")
            prio = int(input("Enter task priority: "))
            scheduler.add_task(desc, prio)
        elif choice == "2":
            desc = input("Enter task description to remove: ")
            scheduler.remove_task(desc)
        elif choice == "3":
            desc = input("Enter task description to search: ")
            scheduler.search_task(desc)
        elif choice == "4":
            scheduler.display_tasks()
        elif choice == "5":
            scheduler.save_to_file("tasks.pkl")
            print("Exiting Task Scheduler.")
            break
        else:
            print("Invalid choice. Please try again.")
