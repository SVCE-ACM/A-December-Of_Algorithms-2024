public class Day11_java_Hari7467
{
    private static boolean checkorigin(String moves)
    {
        int x=0,y=0;
        for(int i=0;i<moves.length();i++)
        {
            char move=moves.charAt(i);
            if(move=='L'){
                x--;
            }
            else if(move=='R'){
                x++;
            }
            else if(move=='U'){
                y++;
            }else
            {
                y--;
            }
        }
        return (x==0 && y==0)?true:false;
    }
    public static void main(String[] args)
    {
        String moves="LRUD";
        System.out.println(checkorigin(moves));
        
    }
}
