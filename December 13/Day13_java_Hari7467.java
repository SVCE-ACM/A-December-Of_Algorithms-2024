import java.util.Scanner;
public class Day13_java_Hari7467 {
    static Scanner sc=new Scanner(System.in);
    public static int find_min_swap(int[] unique_int)
    {
        int min_index,min_value,swaps=0;
        for(int i=0;i<unique_int.length-1;i++)
        {
            min_index=i;
            min_value=unique_int[i];
            for(int j=i+1;j<unique_int.length;j++)
            {
                if(min_value>unique_int[j])
                {
                    min_index=j;
                    min_value=unique_int[j];
                }
            }
            if(min_index!=i)
            {
                int temp=unique_int[i];
                unique_int[i]=unique_int[min_index];
                unique_int[min_index]=temp;
                swaps++;
            }
        }
        return swaps;
    }
    public static void main(String[] args) {
        System.out.print("Enter the number of elements: ");
        int n = sc.nextInt();
        int unique_int[]=new int[n];
        System.out.print("Enter list elements:");
        for(int i=0;i<n;i++)
        {
            unique_int[i]=sc.nextInt();
        } 
        System.out.println(find_min_swap(unique_int));
    }
}
