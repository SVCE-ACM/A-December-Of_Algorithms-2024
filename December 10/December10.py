tasks = []
n = int(input())
for _ in range(n):
    task_name = input()
    dependencies = input().split(",") if input().strip() else []
    tasks.append((task_name.strip(), [d.strip() for d in dependencies if d.strip()]))

result = []

def checkDependencies(tasks):
    while tasks:
        temp = []
        for task in tasks:
            if not task[1]:  
                temp.append(task[0])
        if not temp:
            print("Error: Cyclic dependency detected")
            return
        result.append(temp)
        tasks = [
            (task[0], [dep for dep in task[1] if dep not in temp])
            for task in tasks
            if task[0] not in temp
        ]
    print(result)
checkDependencies(tasks)