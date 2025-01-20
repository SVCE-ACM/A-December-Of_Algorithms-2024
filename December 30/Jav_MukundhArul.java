class SuperEggDrop {
    public static int superEggDrop(int k, int n) {
        int[][] dp = new int[k + 1][n + 1];

        for (int moves = 1; moves <= n; moves++) {
            for (int eggs = 1; eggs <= k; eggs++) {
                dp[eggs][moves] = dp[eggs - 1][moves - 1] + dp[eggs][moves - 1] + 1;
                if (dp[eggs][moves] >= n) {
                    return moves;
                }
            }
        }

        return n;
    }

    public static void main(String[] args) {
        System.out.println(superEggDrop(2, 6));  // Output: 3
        System.out.println(superEggDrop(3, 14)); // Output: 4
    }
}
