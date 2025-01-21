import java.util.*;
import java.lang.*;

public class JosephusProblem
{
    static int numberOfPeople()
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of people: ");
        int number = sc.nextInt();
        return number;
    }

    static String[] inputArray(int size)
    {
        Scanner sc = new Scanner(System.in);

        String array[] = new String[size];
        int ctrl;

        for(ctrl = 0; ctrl < size; ctrl++)
        {
            int i = ctrl +1;
            System.out.println("Enter the element-" + i +": ");
            array[ctrl] = sc.next();
        }
        return array;
    }

    static void display(String array[], int size)
    {
        int ctrl;
    
        for(ctrl = 0; ctrl < size; ctrl++)
        {
            System.out.print(array[ctrl] + "\t");
        }
    }

    static int safePosition(String array[], int size)
    {
        int ctrl, idx = 0;
        for(ctrl = 0; ctrl < size; ctrl++)
        {
            if(array[ctrl].equalsIgnoreCase("Done") == false)
            {
                idx = ctrl + 1;
            }
        }
        return idx;
    }

    public static void main(String args[])
    { 
        Scanner sc = new Scanner(System.in);

        int size = numberOfPeople();
        String input[] = inputArray(size);
        String temp[] = new String[size - 1];
        int ctrl = 0, ctrl1 = 0, counter = 1, i = 1;
        System.out.println("Enter the value of k: ");
        int k = sc.nextInt();

        while(temp[size-2] == null)
        {
            // System.out.println("\n");
            // System.out.println("Iteration: " + i);

            while(ctrl < size)
            {
                // System.out.println("\nctrl: " + ctrl);
                // System.out.println("\nCounter: " + counter);

                if(counter != k && input[ctrl].equalsIgnoreCase("Done") == false) 
                {
                    // System.out.println("1st if");
                    ctrl++;
                    counter++;
                }

                else if(counter !=k && input[ctrl].equalsIgnoreCase("Done") == true)
                {
                    ctrl++;
                    // System.out.println("1st else if");
                }

                else if(counter == k && input[ctrl].equalsIgnoreCase("Done") == false)
                {
                    // System.out.println("2nd else if");
                    counter = 1;
                    temp[ctrl1] = input[ctrl];
                    // display(temp, size-1);
                    // System.out.println("\n");
                    ctrl1++;
                    input[ctrl] = "Done";
                    // display(input, size);
                    ctrl++;
                }

                else if(counter == k && input[ctrl].equalsIgnoreCase("Done") == true)
                {
                    // System.out.println("3rd else if");
                    ctrl++;
                }
            }
            i++;

            if(ctrl == size && counter < k)
            {
                if(counter == 1)
                {
                    // System.out.println("1st outer if inner if");
                    ctrl = 0;
                }
                else
                {
                    // System.out.println("1st outer if inner else  ");
                    ctrl = 0;
                    counter++;
                }
            }

            else if(ctrl == size && counter == k)
            {
                // System.out.println("2nd outer else if");
                ctrl = 0;
            }
            
        }
        int result = safePosition(input, size);
        System.out.println("The player should stand at " + result + " to survive the game.");
    }
}