import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
public class Day9_java_Hari7467 {
    public static void main(String[] args) {
        List<Integer> returns=new ArrayList<>(Arrays.asList(2, 1, 5, 1, 0, 3, 1, 4, 1));
        int cus_count=0;
        for(int frequency:returns)
        {
            if(frequency==1) cus_count++;
        }
        System.out.println(cus_count);
    }
}
