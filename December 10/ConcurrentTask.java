import java.util.*;

public class ConcurrentTask 
{
    public static void main(String[] args) 
    {
        Scanner sc = new Scanner(System.in);
        ArrayList<String> taskList = new ArrayList<>();
        ArrayList<Integer> numDependency = new ArrayList<>();
        ArrayList<ArrayList<String>> task = new ArrayList<>();

        int i, j, k;
        System.out.print("\nEnter the number of tasks: ");
        int numberOfTasks = sc.nextInt();
        sc.nextLine();

        for(i = 0; i < numberOfTasks; i++)
        {
            System.out.printf("\nEnter the name of task-%d: ", i + 1);
            String taskName = sc.nextLine();
            taskList.add(taskName);

            System.out.print("\n\tEnter the number of dependencies: ");
            int noOfDependencies = sc.nextInt();
            sc.nextLine();
            numDependency.add(noOfDependencies);
            ArrayList<String> dependencies = new ArrayList<>();

            for(j = 0; j < noOfDependencies; j++)
            {
                System.out.printf("\n\t\tEnter dependency-%d: ", j + 1);
                String element = sc.nextLine();
                dependencies.add(element);
            }

            task.add(dependencies);
        }

        int flag = 0;
        for(i = 0; i < numberOfTasks - 1; i++)
        {
            int size = numDependency.get(i);
            ArrayList<String> taskDependencies = task.get(i);
            for(j = 0; j < size; j++)
            {
                String e1 = taskDependencies.get(j);
                int flag1 = 0;
                for(k = i + 1; k < numberOfTasks; k++)
                {
                    String e2 = taskList.get(k);
                    if(e1.equals(e2) == true)
                        flag1 = 1;
                        break;
                }

                if(flag1 == 1)
                {
                    flag = 1;
                    break;
                }
            }
            if(flag == 1)
                System.out.println("Error: Cyclic Dependency detected");
                break;
        }
        
        if (flag == 0)
        {
            ArrayList<ArrayList<String>> taskExecution = new ArrayList<>();
            ArrayList<String> startState = new ArrayList<>();
            startState.add(taskList.get(0));
            taskExecution.add(startState);

            ArrayList<ArrayList<String>> tempTask = new ArrayList<>();
            ArrayList<String> tempTaskList = new ArrayList<>();
            tempTask = task;
            tempTaskList = taskList;

            for(i = 1; i < tempTask.size(); i++)
            {
                ArrayList<String> list1 = new ArrayList<>();
                list1 = tempTask.get(i);
                ArrayList<String> state = new ArrayList<>();
                state.add(tempTaskList.get(i));
                int n = i + 1;

                while(n < tempTask.size())
                {
                    ArrayList<String> list2 = new ArrayList<>();
                    list2 = tempTask.get(n);
                    if(list1.equals(list2) == true)
                    {
                        state.add(tempTaskList.get(n));
                        tempTask.remove(n);
                        tempTaskList.remove(n);
                    }
                    
                    else
                    
                        n++;
                }
                taskExecution.add(state);
            }

            System.out.println(taskExecution);
            
            
        } 
    }
}