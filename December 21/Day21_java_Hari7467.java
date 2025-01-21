import java.util.LinkedList;
import java.util.Scanner;

class Day21_java_Hari7467 {
    static Scanner sc=new Scanner(System.in);
    static LinkedList<Integer> list1=new LinkedList<>();
    static LinkedList<Integer> list2=new LinkedList<>();
    static void add_list1(int n)
    {
        System.out.println("ENter node values:");
        for(int i=0;i<n;i++)
        {
            list1.add(sc.nextInt());
        }
    }
    static void add_list2(int n)
    {
        System.out.println("ENter node values:");
        for(int i=0;i<n;i++)
        {
            list2.add(sc.nextInt());
        }
    }
    static LinkedList<Integer> extract_list(LinkedList<Integer> list,int pos)
    {
        LinkedList<Integer> temp_list=new LinkedList<>();
        for(int i=pos-1;i<list.size();i++){
            temp_list.add(list.get(i));
        }
        return temp_list;
    }
    static void align(int pos)
    {
        if(list1.size()<list2.size())
        {
             list1.addAll(extract_list(list2,pos));
        }else{
            list2.addAll(extract_list(list1,pos));
        }
    }
    static int find_intersect(LinkedList<Integer> list1,LinkedList<Integer> list2,int diff)
    {
        for(int i=0;i<list1.size();i++)
        {
            if(list1.get(i)==list2.get(i+diff))
            {
                return i+1;
            }
        }
        return 0;
    }
    static int  make_intersect(int pos)
    {
         align(pos);
         if(list1.size()>list2.size())
         {
            int diff=list1.size()-list2.size();
            return find_intersect(list2,list1,diff);
         }else{
            int diff=list2.size()-list1.size();
            return find_intersect(list1,list2,diff);
         }

    }
    public static void main(String[] args) {
        System.out.println("ENter list1 length:");
        int l1=sc.nextInt();
        add_list1(l1);
        System.out.println("ENter list2 length:");
        int l2=sc.nextInt();
        add_list2(l2);
        System.out.println();
        System.out.println("Enter the position to intersect:");
        int pos=sc.nextInt();
        if(pos>0)
        {
            System.out.println(make_intersect(pos));
        }
        else{
            System.out.println("NOT INTERSECT");
        }
    }
}
