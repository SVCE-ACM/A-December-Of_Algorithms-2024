10 REM Initialize arrays and variables
20 DIM graph(100, 100), in_degree(100), queue(100), result(100, 100), concurrent_tasks(100)
30 task_count = 0
40 result_count = 0

50 REM Get number of tasks and dependencies
60 PRINT "Enter number of tasks: ";
70 INPUT n

80 REM Initialize in_degree array
90 FOR i = 1 TO n
100    in_degree(i) = 0
110 NEXT i

120 REM Get task dependencies
130 PRINT "Enter task dependencies (task followed by its dependencies):"
140 FOR i = 1 TO n
150    PRINT "Enter task and number of dependencies for task "; i; ": ";
160    INPUT task, m
170    FOR j = 1 TO m
180        PRINT "Enter dependency: ";
190        INPUT dependency
200        graph(dependency, task) = 1
210        in_degree(task) = in_degree(task) + 1
220    NEXT j
230 NEXT i

240 REM Initialize queue with tasks having no dependencies
250 front = 1
260 rear = 0
270 FOR i = 1 TO n
280    IF in_degree(i) = 0 THEN
290        rear = rear + 1
300        queue(rear) = i
310    END IF
320 NEXT i

330 REM Process tasks and check for cyclic dependencies
340 WHILE front <= rear
350    task_count = 0
360    WHILE front <= rear
370        task = queue(front)
380        front = front + 1
390        concurrent_tasks(task_count) = task
400        task_count = task_count + 1
410        FOR i = 1 TO n
420            IF graph(task, i) = 1 THEN
430                in_degree(i) = in_degree(i) - 1
440                IF in_degree(i) = 0 THEN
450                    rear = rear + 1
460                    queue(rear) = i
470                END IF
480            END IF
490        NEXT i
500    WEND

510    FOR i = 1 TO task_count - 1
520        result(result_count, i) = concurrent_tasks(i)
530    NEXT i
540    result_count = result_count + 1
550 WEND

560 REM Check for cyclic dependencies
570 FOR i = 1 TO n
580    IF in_degree(i) > 0 THEN
590        PRINT "Error: Cyclic dependency detected"
600        END
610    END IF
620 NEXT i

630 REM Output the task order
640 PRINT "Task order:"
650 FOR i = 1 TO result_count
660    PRINT "Concurrent tasks for level "; i; ": ";
670    FOR j = 1 TO n
680        IF result(i, j) <> 0 THEN
690            PRINT result(i, j); " ";
700        END IF
710    NEXT j
720    PRINT ""
730 NEXT i
