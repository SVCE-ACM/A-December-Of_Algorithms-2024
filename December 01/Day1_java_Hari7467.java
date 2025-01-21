public class Day1_java_Hari7467 {
    
    private static int find_missing_value(int race[])
    {
        int start=race[0];
        for(int i=0;i<race.length;i++)
        {
            if(start==race[i])
            {
                start++;
            }
            else
            {
                return start;
            }
        }
        return 0;
    }
    public static void main(String[] args)
    {
        int race[]={100,101,102,104,105};
        System.out.println(Day1_java_Hari7467.find_missing_value(race));
    }
}
