
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class Day14_java_Hari7467
{
    static Scanner sc=new Scanner(System.in);
    public static int find_unique(List<Integer> students)
    {
       Map<Integer,Integer> unique=new HashMap<>();
       for(int stu:students)
       {
        unique.put(stu,unique.getOrDefault(stu, 0)+1);
       }
       return unique.size();
    }
    public static boolean partition(List<Integer> students,int K,int D)
    {
        Map<Integer,Integer> team_1=new HashMap<>();
        Map<Integer,Integer> team_2=new HashMap<>();
        Iterator<Integer> iterator=students.iterator();
        while (iterator.hasNext())
         {
           
            int stu=iterator.next();
            if(!team_1.containsKey(stu) && team_1.size()<=K)
            {
                team_1.put(stu,1);
                iterator.remove();
            }
            else if(!team_1.containsKey(stu) && !team_2.containsKey(stu) && team_2.size()<=K)
            {
                team_2.put(stu,1);
                iterator.remove();
            }
            else if(team_1.size()>K && team_2.size()>K)
            {
                break;
            }
        }
        for(int i=0;i<students.size();i++)
        {
            if(i%2==0)
            {
                team_1.put(students.get(i),1);
            }
            else{
                team_2.put(students.get(i),1);
            }
        }
        return (Math.abs(team_1.size()-team_2.size())<=D)?true:false;

    }
    public static void main(String[] args) {
        int i=1;
        List<Integer> students=new ArrayList<>();
        System.out.println("Enter T:");
        int T=sc.nextInt();
        while(i<=T)
        {
            System.out.println("TEST CASE : "+i);
            System.out.println("Enter N K D:");
            int N=sc.nextInt(),K=sc.nextInt(),D=sc.nextInt();
            System.out.println("Enter N Students:");
            for(int j=0;j<N;j++)
            {
                students.add(sc.nextInt());
            }
            int unique=find_unique(students);
            if(unique==(2*K)){
                if(partition(students,K,D))
                {
                    System.out.println("YES");
                }
            }
            else{
                System.out.println("NO");
            }
            i++;
        }
        
    }
}