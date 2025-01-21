import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;

public class Day10_java_Hari7467 {
    static private Map<Character,List<Character>> adjencymap=new HashMap<>();
    static private Map<Character,Integer> in_degree=new HashMap<>();
    static private Queue<Character> queue=new LinkedList<>();
    static private List<List<Character>> list=new ArrayList<>();
    static int i=0;
    static boolean terminator=false;
    public static void addedge(Character source,List<Character> list_destination)
    {
        adjencymap.putIfAbsent(source,new ArrayList<>());
        for(Character destination:list_destination)
        {
            adjencymap.putIfAbsent(destination,new ArrayList<>());
            adjencymap.get(source).add(destination);
        }
    }
    public static boolean indegree()
    {
        for(Map.Entry<Character,List<Character>> vertex:adjencymap.entrySet())
        {
            in_degree.put(vertex.getKey(),vertex.getValue().size());
            if(vertex.getValue().size()==0) terminator=true;
        }
        return terminator;
    }
    public static void addqueue()
    {
        boolean temp=true;
        for(Map.Entry<Character,Integer> depend:in_degree.entrySet())
        {
            if(depend.getValue()==0)
            {
                if(temp)
                {
                    list.add(new ArrayList<>());
                    temp=false;
                }
                queue.add(depend.getKey());
                list.get(i).add(depend.getKey());
                in_degree.put(depend.getKey(),-1);
            }
        }
        if(!temp) i++;
    }
    public static void reduceindegree(Character task)
    {
        terminator = task==null?false:true;
        for(Map.Entry<Character,List<Character>> popdepency:adjencymap.entrySet())
        {
            for(Character depended_task:popdepency.getValue())
            {
                if(depended_task.equals(task))
                {
                   for(Map.Entry<Character,Integer> decrement:in_degree.entrySet())
                   {
                        if(popdepency.getKey().equals(decrement.getKey()))
                        {
                            in_degree.put(decrement.getKey(),decrement.getValue()-1);
                        }
                   }
                }
            }
        }
    }
    public static boolean process()
    {
        if(!indegree())
        {
            return false;
        }
        else
        {
            while(terminator)
            {
                addqueue();
                reduceindegree(queue.poll());
            }
        }
        return true;
    }
    public static void printlist()
    {
        for(List<Character> row :list)
        {
            System.out.print(row);
        }
    }
    public static void main(String[] args) {
            HashMap<Character,List<Character>> tasks=new HashMap<>();
            tasks.put('A',new ArrayList<>(Arrays.asList('B')));
            tasks.put('B',new ArrayList<>(Arrays.asList('A')));
           
            for(Map.Entry<Character,List<Character>> task:tasks.entrySet())
            {
                addedge(task.getKey(),task.getValue());
            } 
            if(process())
            {
                printlist();   
            }  
            else
            {
                System.out.println("Error: Cyclic dependency detected");
            }
            
    }
}
