public class Day18_java_Hari7467 {
    public static String longestPalindrome(String s) {
        
        StringBuilder str = new StringBuilder();
        str.append("^"); 
        for (int i = 0; i < s.length(); i++) {
            str.append("#");
            str.append(s.charAt(i));
        }
        str.append("#$"); 

        int n = str.length();
        int[] P = new int[n];  
        int center = 0, right = 0;

        for (int i = 1; i < n - 1; i++)
        {
            int mirror = 2 * center - i;

            if (i < right) {
                P[i] = Math.min(right - i, P[mirror]);
            }

            while (str.charAt(i + P[i] + 1) == str.charAt(i - P[i] - 1)) {
                P[i]++;
            }

            if (i + P[i] > right) {
                center = i;
                right = i + P[i];
            }
        }
        int maxLen = 0, maxCenter = 0;
        for (int i = 1; i < n - 1; i++) {
            if (P[i] > maxLen) {
                maxLen = P[i];
                maxCenter = i;
            }
        }
        int start = (maxCenter - maxLen) / 2;
        return s.substring(start, start + maxLen);
    }

    public static void main(String[] args) {
        String input = "DERRREDERREDEREDR";
        String str=longestPalindrome(input);
        int D=500,R=250,E=100,profit=0;
        for(int i=0;i<str.length();i++)
        {
            char c=str.charAt(i);
            if(c=='D'){
                profit+=D;
            }
            else if(c=='R'){
                profit+=R;
            }
            else{
                profit+=E;
            }
        }
        System.out.println("$ "+ profit*str.length());
    }
}
