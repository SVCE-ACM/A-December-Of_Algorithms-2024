public class Day4_java_Hari7467 {
    public static void main(String []args)
    {
        int a=0,b=1,c=0,n=12;
        if(n<=1) c=1;
        while(n>1)
        {
            c=a+b;
            a=b;
            b=c;
            n--;
        }
        System.out.println(c);
    }
}
