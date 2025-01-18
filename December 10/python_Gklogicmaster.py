rom collections import defaultdict, deque

def determine_execution_order(tasks):
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    
    for task_id, dependencies in tasks:
        if task_id not in in_degree:
            in_degree[task_id] = 0
        for dep in dependencies:
            graph[dep].append(task_id)
            in_degree[task_id] += 1
    queue = deque([task for task in in_degree if in_degree[task] == 0])
    if not queue:
        return "Error: Cyclic dependency detected"

    result = []
    while queue:
        level = []
        for _ in range(len(queue)):
            task = queue.popleft()
            level.append(task)

            for neighbor in graph[task]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        result.append(level)
    if any(in_degree[task] > 0 for task in in_degree):
        return "Error: Cyclic dependency detected"

    return result

def get_user_tasks():
    tasks = []
    print("Enter tasks and their dependencies in the format 'Task:Dep1,Dep2,...'. Type 'done' to finish.")
    while True:
        user_input = input("Enter task: ").strip()
        if user_input.lower() == 'done':
            break
        if ":" in user_input:
            task_id, dependencies = user_input.split(":")
            dependencies = dependencies.split(",") if dependencies else []
        else:
            task_id = user_input
            dependencies = []
        tasks.append((task_id.strip(), [dep.strip() for dep in dependencies]))
    return tasks

if _name_ == "_main_":
    print("Provide the list of tasks and dependencies:")
    tasks = get_user_tasks()
    output = determine_execution_order(tasks)
    print(output)
