import heapq
import pickle
import os

class TaskScheduler:
    def __init__(self, filename="tasks.pkl"):
        self.heap = []
        self.task_map = {}
        self.filename = filename
        self.load_tasks()

    def add_task(self, description, priority):
        if description in self.task_map:
            print(f"Task '{description}' already exists.")
            return
        task = (-priority, description)
        heapq.heappush(self.heap, task)
        self.task_map[description] = task
        self.save_tasks()

    def remove_task(self, description):
        if description not in self.task_map:
            print(f"Task '{description}' not found.")
            return
        self.heap.remove(self.task_map[description])
        heapq.heapify(self.heap)
        del self.task_map[description]
        self.save_tasks()

    def search_task(self, description):
        return self.task_map.get(description, None)

    def display_tasks(self):
        return [(desc, -priority) for priority, desc in sorted(self.heap)]

    def save_tasks(self):
        with open(self.filename, "wb") as f:
            pickle.dump((self.heap, self.task_map), f)

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "rb") as f:
                self.heap, self.task_map = pickle.load(f)
                heapq.heapify(self.heap)

scheduler = TaskScheduler()
scheduler.add_task("Complete Assignment", 2)
scheduler.add_task("Buy Groceries", 1)
print("Tasks:", scheduler.display_tasks())
scheduler.remove_task("Complete Assignment")
print("Tasks after removal:", scheduler.display_tasks())
