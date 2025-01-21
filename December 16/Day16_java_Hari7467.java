
import java.util.Arrays;
public class Day16_java_Hari7467 {
    public static void sort(int[] arrival,int[] depart)
    {
        Arrays.sort(arrival);
        Arrays.sort(depart);
    }
    public static int find_min_platform(int[] arrival,int[] depart)
    {
        int  platforms_in_use = 0;
        int  max_platforms = 0;
        for(int i=1;i<arrival.length;i++)
        {
            for(int j=1;j<depart.length;j++)
            {
                if(arrival[i]<=depart[j])
                {
                    platforms_in_use++;
                    max_platforms=Math.max(max_platforms,platforms_in_use);
                    break;
                }else{
                    platforms_in_use--;
                }
            }
        }
        return max_platforms;
    }
    public static void main(String[] args) {
        int arrival[]={1030, 1015, 1045, 1100, 1500, 1530};
        int depart[]={1040, 1105, 1050, 1130, 1515, 1600};
        sort(arrival,depart);
        System.out.println("Minimum Platform Required:"+find_min_platform(arrival,depart));
    }
}
