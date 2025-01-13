from collections import defaultdict, deque

def Exec_Ordr(tasks):
    graph = defaultdict(list)
    in_deg = defaultdict(int)
    
    for task, dependencies in tasks:
        in_deg[task]
        for dep in dependencies:
            graph[dep].append(task)
            in_deg[task] += 1

    queue = deque([task for task in in_deg if in_deg[task] == 0])
    result = []
    
    while queue:
        current_batch = []
        for _ in range(len(queue)):
            task = queue.popleft()
            current_batch.append(task)
            
            for neighbor in graph[task]:
                in_deg[neighbor] -= 1
                if in_deg[neighbor] == 0:
                    queue.append(neighbor)
        
        result.append(current_batch)
    
    if sum(len(batch) for batch in result) != len(tasks):
        return "Error: Cyclic dependency detected"
    
    return result

if __name__ == "__main__":
    n = int(input("Enter the number of tasks: "))
    tasks = []
    
    for _ in range(n):
        task_id = input(f"Enter Task ID for Task {_+1}: ")
        dependencies = input(f"Enter dependencies @Task {task_id}: ")
        dependencies = dependencies.split(",") if dependencies else []
        tasks.append((task_id, dependencies))
    
    output = Exec_Ordr(tasks)
    
    if isinstance(output, str):
        print(output)
    else:
        print("Execution Order:")
        for i, batch in enumerate(output, 1):
            print(f"Step {i}: {batch}")

