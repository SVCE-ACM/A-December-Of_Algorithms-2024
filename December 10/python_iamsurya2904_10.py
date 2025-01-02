from collections import defaultdict, deque

def find_task_order(tasks):
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    for task, dependencies in tasks:
        for dependency in dependencies:
            graph[dependency].append(task)
            in_degree[task] += 1

    queue = deque([task for task, degree in in_degree.items() if degree == 0])
    result = []

    while queue:
        concurrent_tasks = []
        for _ in range(len(queue)):
            task = queue.popleft()
            concurrent_tasks.append(task)
            for neighbor in graph[task]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        result.append(concurrent_tasks)

    if any(degree > 0 for degree in in_degree.values()):
        return "Error: Cyclic dependency detected"

    return result

