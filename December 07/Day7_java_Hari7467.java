import java.util.ArrayList;
import java.util.List;
public class Day7_java_Hari7467 {
    public static void main(String[] args) {
        List<List<Integer>> list=new ArrayList<>();
        int n=2;
        for(int i=0;i<n;i++)
        {
            list.add(new ArrayList<>());

            for(int j=0;j<=i;j++)
            {
                if(j==0 || j==i)
                {
                    list.get(i).add(1);
                }
                else
                {
                    int ele=list.get(i-1).get(j-1)+list.get(i-1).get(j);
                    list.get(i).add(ele);
                }
            }
        }
        for(List<Integer> row :list)
        {
            System.out.println(row);
        }
       
    }
}
