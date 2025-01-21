import java.util.ArrayList;
import java.util.List;

public class Day5_java_Hari7467 {
    public  int simulateSafePosition(List<Integer> circle, int k) {

        int index = 0; 
        while (circle.size() > 1) {
            index = (index + k - 1) % circle.size(); 
            circle.remove(index);
        }

        return circle.get(0);
    }
    public static void main(String[] args) {
        int n=3,k=2;
        Day5_java_Hari7467 obj=new Day5_java_Hari7467();
        List<Integer> circle=new ArrayList<>();
        for(int i=1;i<=n;i++)
        {
            circle.add(i);
        }
        System.out.println(obj.simulateSafePosition(circle,k));

    
}
}

