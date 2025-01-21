public class Day27_java_Hari7467 {
    public static void main(String[] args) {
        int height[]={4,2,0,3,2,5};
        int len=height.length,max=0,trap_water=0;
        int max_left[]=new int[len];
        int max_right[]=new int[len];
        for(int i=0;i<len;i++)
        {
            if(max>height[i])
            {
                max_right[i]=max;

            }else{
                max=height[i];
                max_right[i]=max;
            }
        }
        max=0;
        for(int i=len-1;i>=0;i--)
        {
            if(max>height[i])
            {
                max_left[i]=max;
            }else{
                max=height[i];
                max_left[i]=max;
            }
        }
        for(int i=0;i<len;i++)
        {
            trap_water+=Math.min(max_left[i],max_right[i])-height[i];
        }
        System.out.println(trap_water);
    }
}
