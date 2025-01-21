def task_execution_order(tasks):
    graph = {}
    in_degree = {}

    for task, dependencies in tasks:
        graph[task] = []
        in_degree[task] = 0

    for task, dependencies in tasks:
        for dep in dependencies:
            graph[dep].append(task)
            in_degree[task] += 1

    no_dependency = [task for task in in_degree if in_degree[task] == 0]
    execution_order = []

    while no_dependency:
        current_layer = no_dependency[:]
        no_dependency = []
        execution_order.append(current_layer)

        for task in current_layer:
            for neighbor in graph[task]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    no_dependency.append(neighbor)

    if any(in_degree[task] > 0 for task in in_degree):
        return "Error: Cyclic dependency detected"

    return execution_order

tasks1 = [
    ("A", []),
    ("B", ["A"]),
    ("C", ["A"]),
    ("D", ["B", "C"]),
    ("E", ["D"])
]

tasks2 = [
    ("A", ["B"]),
    ("B", ["A"])
]

print(task_execution_order(tasks1))  
print(task_execution_order(tasks2)) 
