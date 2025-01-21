public class Day30_java_Hari7467 {
        static int minMoves(int eggs, int floors) {
            int[][] dp = new int[eggs + 1][floors + 1];
    
            for (int i = 1; i <= floors; i++) {
                dp[1][i] = i;
            }
            for (int k = 2; k <= eggs; k++) {
                for (int n = 1; n <= floors; n++) {
                    dp[k][n] = Integer.MAX_VALUE;
    
                    for (int x = 1; x <= n; x++) {
                        int res = 1 + Math.max(dp[k-1][x-1], dp[k][n-x]);
                        dp[k][n] = Math.min(dp[k][n], res);
                    }
                }
            }
            return dp[eggs][floors];
        }
        public static void main(String[] args) {
            int eggs = 3;         
            int floors = 14;      
    
            System.out.println("Minimum moves required: " + minMoves(eggs, floors));
        }
    }
    