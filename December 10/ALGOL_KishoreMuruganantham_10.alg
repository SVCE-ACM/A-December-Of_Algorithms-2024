begin
    integer array graph[100, 100];
    integer array in_degree[100];
    integer queue[100], result[100, 100], concurrent_tasks[100];
    integer task, dependency, i, j, n, m, front, rear, task_count, result_count;

    print("Enter number of tasks: ");
    read(n);

    for i := 1 step 1 until n do
        in_degree[i] := 0;

    print("Enter task dependencies (task followed by its dependencies): ");
    for i := 1 step 1 until n do
        begin
            read(task, m);
            for j := 1 step 1 until m do
                begin
                    read(dependency);
                    graph[dependency, task] := 1;
                    in_degree[task] := in_degree[task] + 1;
                end;
        end;

    front := 1;
    rear := 0;
    task_count := 0;
    for i := 1 step 1 until n do
        if in_degree[i] = 0 then
            begin
                rear := rear + 1;
                queue[rear] := i;
            end;

    result_count := 0;
    while front <= rear do
        begin
            task_count := 0;
            while front <= rear do
                begin
                    task := queue[front];
                    front := front + 1;
                    concurrent_tasks[task_count] := task;
                    task_count := task_count + 1;
                    for i := 1 step 1 until n do
                        if graph[task, i] = 1 then
                            begin
                                in_degree[i] := in_degree[i] - 1;
                                if in_degree[i] = 0 then
                                    begin
                                        rear := rear + 1;
                                        queue[rear] := i;
                                    end;
                            end;
                end;

            for i := 0 step 1 until task_count - 1 do
                result[result_count, i] := concurrent_tasks[i];
            result_count := result_count + 1;
        end;

    for i := 1 step 1 until n do
        if in_degree[i] > 0 then
            begin
                print("Error: Cyclic dependency detected");
                return;
            end;

    print("Task order: ");
    for i := 1 step 1 until result_count do
        begin
            print("Concurrent tasks for level ", i, ": ");
            for j := 0 step 1 until n do
                if result[i, j] <> 0 then
                    print(result[i, j], " ");
            print("");
        end;
end.
