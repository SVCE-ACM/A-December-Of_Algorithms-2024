from collections import defaultdict, deque

def find_task_order(tasks):
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    for task, dependencies in tasks:
        for dep in dependencies:
            graph[dep].append(task)
            in_degree[task] += 1
        in_degree.setdefault(task, 0)
    queue = deque([task for task in in_degree if in_degree[task] == 0])
    result = []
    while queue:
        current_level = []
        for _ in range(len(queue)):
            task = queue.popleft()
            current_level.append(task)
            for neighbor in graph[task]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        result.append(current_level)
    return result if sum(in_degree.values()) == 0 else "Error: Cyclic dependency detected"

def get_tasks_from_user():
    n = int(input("Enter the number of tasks: "))
    tasks = [
        (input("Task ID: "), input("Dependencies (comma-separated, leave blank if none): ").split(",") if input("Dependencies (comma-separated, leave blank if none): ").strip() else [])
        for _ in range(n)
    ]
    return tasks

if __name__ == "__main__":
    user_tasks = get_tasks_from_user()
    print("Output:", find_task_order(user_tasks))