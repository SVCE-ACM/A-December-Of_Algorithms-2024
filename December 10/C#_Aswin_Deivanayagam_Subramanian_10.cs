using System;
using System.Collections.Generic;

class Program
{
    static List<List<int>> FindTaskOrder(List<Tuple<int, List<int>>> tasks)
    {
        var graph = new Dictionary<int, List<int>>();
        var inDegree = new Dictionary<int, int>();

        foreach (var task in tasks)
        {
            int taskId = task.Item1;
            List<int> dependencies = task.Item2;
            foreach (var dependency in dependencies)
            {
                if (!graph.ContainsKey(dependency))
                {
                    graph[dependency] = new List<int>();
                }
                graph[dependency].Add(taskId);

                if (!inDegree.ContainsKey(taskId))
                {
                    inDegree[taskId] = 0;
                }
                inDegree[taskId]++;
            }

            if (!inDegree.ContainsKey(taskId))
            {
                inDegree[taskId] = 0;
            }
        }

        var queue = new Queue<int>();
        foreach (var task in inDegree)
        {
            if (task.Value == 0)
            {
                queue.Enqueue(task.Key);
            }
        }

        var result = new List<List<int>>();

        while (queue.Count > 0)
        {
            var concurrentTasks = new List<int>();
            int currentQueueSize = queue.Count;
            for (int i = 0; i < currentQueueSize; i++)
            {
                int task = queue.Dequeue();
                concurrentTasks.Add(task);
                if (graph.ContainsKey(task))
                {
                    foreach (var neighbor in graph[task])
                    {
                        inDegree[neighbor]--;
                        if (inDegree[neighbor] == 0)
                        {
                            queue.Enqueue(neighbor);
                        }
                    }
                }
            }
            result.Add(concurrentTasks);
        }

        if (inDegree.Values.Contains(1))
        {
            return new List<List<int>> { new List<int> { -1 } }; // Error: Cyclic dependency detected
        }

        return result;
    }

    static void Main()
    {
        var tasks = new List<Tuple<int, List<int>>>()
        {
            new Tuple<int, List<int>>(1, new List<int>{2, 3}),
            new Tuple<int, List<int>>(2, new List<int>{4}),
            new Tuple<int, List<int>>(3, new List<int>{4}),
            new Tuple<int, List<int>>(4, new List<int>())
        };

        var taskOrder = FindTaskOrder(tasks);
        
        if (taskOrder.Count == 1 && taskOrder[0][0] == -1)
        {
            Console.WriteLine("Error: Cyclic dependency detected");
        }
        else
        {
            foreach (var taskBatch in taskOrder)
            {
                Console.WriteLine(string.Join(", ", taskBatch));
            }
        }
    }
}
