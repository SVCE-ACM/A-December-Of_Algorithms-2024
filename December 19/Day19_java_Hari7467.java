
public class Day19_java_Hari7467 {
    static int minimum_steps=0;
    private static void TOP(int N,char source,char helper,char destination)
    {
        if(N==1)
        {
            System.out.println("MOVE DISK 1 FROM "+source+" TO "+ destination);
            minimum_steps++;
            return;
        }
        TOP(N-1,source,destination,helper);
        System.out.println("MOVE DISK "+N+" FROM "+source+" TO "+destination);
        minimum_steps++;
        TOP(N-1,helper,source,destination);
    }
    
    public static void main(String[] args) {
        
        int n=3;
        System.out.println("Sequence of moves:");
        TOP(n,'A','B','C');
        System.out.println("Minimum number of moves: "+minimum_steps);

    }
}
