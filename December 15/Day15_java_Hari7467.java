public class Day15_java_Hari7467 {
    public static void main(String[] args) {
        int w=6;
        int houses[]={2, 3, 5, 2, 1};
        int gifts=0,trip=0;
        for(int i=0;i<houses.length;i++){
            if(gifts+houses[i]>w){
               trip++;
               gifts=0;
            }
            gifts+=houses[i];
        }
        trip+=(gifts>0)?1:0;
        System.out.println(trip);
    }
}
