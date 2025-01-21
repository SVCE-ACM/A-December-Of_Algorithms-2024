import java.util.ArrayList;
import java.util.Arrays;
import java.util.SortedSet;
import java.util.TreeSet;

public class Day28_java_Hari7467 {
    public static void main(String[] args) {
        Integer book[]={1, 2, 3, 6, 2, 3, 4, 7, 8};
        int size=4;
        ArrayList<Integer> list=new ArrayList<>();
        SortedSet<Integer> set=new TreeSet<>();
        Arrays.sort(book);
        list.addAll(Arrays.asList(book));
        while(list.size()>=size)
        {
            for(int i=0;i<list.size();i++)
            {
                if(set.size()<size)
                {
                    if(set.add(list.get(i)))
                    {
                        list.remove(i);
                        i--;
                    }
                }
                else{
                    set.clear();
                    break;
                }
            }
        }
        System.out.println(list.isEmpty());
    }
}
