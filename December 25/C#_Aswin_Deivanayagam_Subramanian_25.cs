using System;
using System.Collections.Generic;
using System.IO;

public class TaskScheduler
{
    private Dictionary<string, TaskNode> tasks; // For constant time search (O(k))
    private SortedList<int, LinkedList<TaskNode>> priorityQueue; // To maintain tasks sorted by priority

    public TaskScheduler()
    {
        tasks = new Dictionary<string, TaskNode>();
        priorityQueue = new SortedList<int, LinkedList<TaskNode>>();
    }

    public void AddTask(string description, int priority)
    {
        var task = new TaskNode(description, priority);

        if (!tasks.ContainsKey(description))
        {
            tasks.Add(description, task);
            if (!priorityQueue.ContainsKey(priority))
            {
                priorityQueue[priority] = new LinkedList<TaskNode>();
            }
            priorityQueue[priority].AddLast(task);
            SaveTasksToFile(); // Save to file after each task addition
        }
        else
        {
            Console.WriteLine("Task already exists.");
        }
    }

    public void RemoveTask(string description)
    {
        if (tasks.ContainsKey(description))
        {
            var task = tasks[description];
            priorityQueue[task.Priority].Remove(task);
            if (priorityQueue[task.Priority].Count == 0)
            {
                priorityQueue.Remove(task.Priority);
            }
            tasks.Remove(description);
            SaveTasksToFile(); // Save after task removal
        }
        else
        {
            Console.WriteLine("Task not found.");
        }
    }

    public void SearchTask(string description)
    {
        if (tasks.ContainsKey(description))
        {
            Console.WriteLine($"Task Found: ({description}, Priority {tasks[description].Priority})");
        }
        else
        {
            Console.WriteLine("Task not found.");
        }
    }

    public void DisplayTasks()
    {
        foreach (var priority in priorityQueue.Reverse())
        {
            foreach (var task in priority.Value)
            {
                Console.WriteLine($"({task.Description}, Priority {task.Priority})");
            }
        }
    }

    private void SaveTasksToFile()
    {
        using (StreamWriter writer = new StreamWriter("tasks.txt"))
        {
            foreach (var task in tasks.Values)
            {
                writer.WriteLine($"{task.Description},{task.Priority}");
            }
        }
    }

    private void LoadTasksFromFile()
    {
        if (File.Exists("tasks.txt"))
        {
            foreach (var line in File.ReadLines("tasks.txt"))
            {
                var parts = line.Split(',');
                var description = parts[0];
                var priority = int.Parse(parts[1]);
                AddTask(description, priority);
            }
        }
    }

    public void Menu()
    {
        LoadTasksFromFile(); // Load tasks from file on startup

        while (true)
        {
            Console.WriteLine("1. Add Task");
            Console.WriteLine("2. Remove Task");
            Console.WriteLine("3. Search Task");
            Console.WriteLine("4. Display Tasks");
            Console.WriteLine("5. Exit");
            Console.Write("Choose an option: ");
            var choice = Console.ReadLine();

            switch (choice)
            {
                case "1":
                    Console.Write("Enter Task Description: ");
                    string description = Console.ReadLine();
                    Console.Write("Enter Task Priority: ");
                    int priority = int.Parse(Console.ReadLine());
                    AddTask(description, priority);
                    break;
                case "2":
                    Console.Write("Enter Task Description to Remove: ");
                    description = Console.ReadLine();
                    RemoveTask(description);
                    break;
                case "3":
                    Console.Write("Enter Task Description to Search: ");
                    description = Console.ReadLine();
                    SearchTask(description);
                    break;
                case "4":
                    DisplayTasks();
                    break;
                case "5":
                    return;
                default:
                    Console.WriteLine("Invalid choice.");
                    break;
            }
        }
    }

    private class TaskNode
    {
        public string Description { get; }
        public int Priority { get; }

        public TaskNode(string description, int priority)
        {
            Description = description;
            Priority = priority;
        }
    }

    public static void Main(string[] args)
    {
        var scheduler = new TaskScheduler();
        scheduler.Menu();
    }
}
