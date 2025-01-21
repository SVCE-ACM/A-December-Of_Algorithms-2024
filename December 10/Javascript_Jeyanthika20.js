function findTaskOrder(tasks) {
    const graph = {};
    const inDegree = {};
    const queue = [];
    const result = [];

    tasks.forEach(([task, dependencies]) => {
        if (!graph[task]) graph[task] = [];
        dependencies.forEach(dep => {
            if (!graph[dep]) graph[dep] = [];
            graph[dep].push(task);
            inDegree[task] = (inDegree[task] || 0) + 1;
        });
    });

    Object.keys(graph).forEach(task => {
        if (!inDegree[task]) queue.push(task);
    });

    while (queue.length) {
        const concurrentTasks = [];
        for (let i = queue.length; i > 0; i--) {
            const task = queue.shift();
            concurrentTasks.push(task);
            if (graph[task]) {
                graph[task].forEach(neighbor => {
                    inDegree[neighbor]--;
                    if (inDegree[neighbor] === 0) queue.push(neighbor);
                });
            }
        }
        result.push(concurrentTasks);
    }

    if (Object.values(inDegree).some(degree => degree > 0)) {
        return "Error: Cyclic dependency detected";
    }

    return result;
}

console.log(findTaskOrder([
    ["A", ["B", "C"]],
    ["B", ["D"]],
    ["C", ["D"]],
    ["D", []]
]));
