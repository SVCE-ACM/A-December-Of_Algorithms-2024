class Day22_java_Hari7467
{
    static int find_max(int b[][])
    {
        int max=1;
        for(int i=0;i<b.length;i++){
            int count=0;
            for(int j=0;j<b.length;j++){
                int x=(b[i][0]-b[j][0]);
                x*=x;
                int y=(b[i][1]-b[j][1]);
                y*=y;
                if(Math.sqrt((x+y))<=b[i][2]) {
                    count++;
                }
            }
            if(max<count){
                max=count;
            }
        }
        return max;
    }
    public static void main(String[] args)
    {
        int building[][]={{1,1,5},{10,10,5}};
        System.out.println(find_max(building));
    }
}
