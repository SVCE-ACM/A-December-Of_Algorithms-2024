public class Day3_java_Hari7467 {
    private  String square(int b,int r)
    {
        StringBuilder res=new StringBuilder();
        if(Math.abs(b-r)>1) return "NOT POSSIBLE";
        while (b>0 || r>0)
        {
            if(b>0 && b>r)
            {
                res.append("B");b--;
                if(r>0)
                {
                    res.append("R");r--;
                } 
            }
            else if(r>0 && r>b)
            {
                res.append("R");r--;
                if(b>0)
                {
                    res.append("B");b--;
                }
            }
            else
            {
                res.append("B");b--;
                res.append("R");r--;
            }
        }
        return res.toString();
    }
    public static void main(String[] args) {
        int b=4,r=4;
        Day3_java_Hari7467 obj=new Day3_java_Hari7467();
        System.out.println(obj.square( b, r));
    }
    
}
