import heapq

class TaskScheduler:
    def __init__(self):
        # Using a min-heap with negative priority for max-heap behavior
        self.task_heap = []
        self.task_map = {}

    def add_task(self, task, priority):
        # Add task to the heap and a hashmap for O(1) lookup
        heapq.heappush(self.task_heap, (-priority, task))
        self.task_map[task] = -priority

    def remove_task(self, task):
        # Remove task from the hashmap and rebuild the heap
        if task in self.task_map:
            del self.task_map[task]
            self.task_heap = [(-p, t) for t, p in self.task_map.items()]
            heapq.heapify(self.task_heap)
        else:
            print(f"Task '{task}' not found.")

    def search_task(self, task):
        # Search for a task in O(1)
        if task in self.task_map:
            return f"Task: '{task}', Priority: {-self.task_map[task]}"
        else:
            return f"Task '{task}' not found."

    def display_tasks(self):
        # Display all tasks sorted by priority
        return [(task, -priority) for priority, task in sorted(self.task_heap, reverse=True)]

# Menu-driven interface
def main():
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
            task = input("Enter task description: ")
            priority = int(input("Enter task priority: "))
            scheduler.add_task(task, priority)
            print(f"Task '{task}' added with priority {priority}.")

        elif choice == "2":
            task = input("Enter task description to remove: ")
            scheduler.remove_task(task)
            print(f"Task '{task}' removed.")

        elif choice == "3":
            task = input("Enter task description to search: ")
            print(scheduler.search_task(task))

        elif choice == "4":
            tasks = scheduler.display_tasks()
            if tasks:
                print("Tasks in priority order:")
                for task, priority in tasks:
                    print(f"Task: '{task}', Priority: {priority}")
            else:
                print("No tasks available.")

        elif choice == "5":
            print("Exiting Task Scheduler.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
