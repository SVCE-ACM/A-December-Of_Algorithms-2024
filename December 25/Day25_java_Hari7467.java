import java.util.*;

class TaskManager {
    private final Map<String, Integer> taskMap = new HashMap<>();

    public void addTask(String task, int priority) {
        taskMap.put(task, priority);
        System.out.println("Task added: " + task + " with priority " + priority);
    }

    public void removeTask(String task) {
        if (taskMap.containsKey(task)) {
            taskMap.remove(task);
            System.out.println("Task removed: " + task);
        } else {
            System.out.println("Task not found.");
        }
    }

    public void displayTasks() {
        if (taskMap.isEmpty()) {
            System.out.println("No tasks to display.");
            return;
        }

        System.out.println("Tasks in Priority Order:");
        taskMap.entrySet()
               .stream()
               .sorted((a, b) -> b.getValue().compareTo(a.getValue())) // Sort by priority descending
               .forEach(entry -> System.out.println("Task: " + entry.getKey() + ", Priority: " + entry.getValue()));
    }
}

public class Day25_java_Hari7467 {
    private static final Scanner sc = new Scanner(System.in);
    private static final TaskManager taskManager = new TaskManager();

    private static void showMenu() {
        System.out.println("Task Scheduler");
        System.out.println("1. Add Task");
        System.out.println("2. Remove Task");
        System.out.println("3. Display Tasks");
        System.out.println("4. Exit");
    }

    public static void main(String[] args) {
        boolean running = true;

        while (running) {
            showMenu();
            System.out.println("Enter your choice:");
            int choice = sc.nextInt();
            sc.nextLine(); // Consume the newline character
            switch (choice) {
                case 1:
                    System.out.println("Enter task description:");
                    String task = sc.nextLine();
                    System.out.println("Enter task priority:");
                    int priority = sc.nextInt();
                    sc.nextLine(); // Consume the newline character
                    taskManager.addTask(task, priority);
                    break;
                case 2:
                    System.out.println("Enter task to remove:");
                    String taskToRemove = sc.nextLine();
                    taskManager.removeTask(taskToRemove);
                    break;
                case 3:
                    taskManager.displayTasks();
                    break;
                case 4:
                    running = false;
                    break;
                default:
                    System.out.println("Please enter a valid option.");
            }
        }
        sc.close();
    }
}
