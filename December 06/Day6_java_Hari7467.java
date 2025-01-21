public class Day6_java_Hari7467 {
    static int x=0;
    public static void pairs(int[][] pair,int i,int j)
    {
        pair[x][0]=i;
        pair[x][1]=j;
        x++;
    }
    public static void main(String[] args) {
        int pair[][]=new int[100][2];
        int numbers[]={2, 4, 3, 7, 1, 5};
        int target=6;
        for(int i=0;i<numbers.length-1;i++)
        {
            for(int j=i;j<numbers.length;j++)
            {
                if(numbers[i]+numbers[j]==target)
                {
                    pairs(pair,numbers[i],numbers[j]);
                }
            }
        }
        for(int i=0;i<x;i++)
        {
            System.out.print("("+pair[i][0]+","+pair[i][1]+")"+",");
        } 
    }
}
