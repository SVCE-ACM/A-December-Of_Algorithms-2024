class Day8_java_Hari7467
{
    static int digitsum(int n)
    {
        int sum=0;
        while(n>0)
        {
            int digit=n%10;
            sum+=(digit*digit);
            n=n/10;
        }
        return sum;
    }
    public static void main(String[] args)
    {
        int n=20,totalsum=0;
        for(int i=1;i<=n;i++)
        {
            totalsum+=digitsum(i);
            
        }
        System.out.println(totalsum);
    }
}