public class Day26_java_Hari7467
{
            public static boolean canJump(int[] nums) {
                return canJumpFromIndex(nums, 0);
            }
            private static boolean canJumpFromIndex(int[] nums, int index) {
                if (index >= nums.length - 1) {
                    return true;
                }
                int maxJump = index + nums[index];
                for (int nextIndex = index + 1; nextIndex <= maxJump; nextIndex++) {
                    if (canJumpFromIndex(nums, nextIndex)) {
                        return true;
                    }
                }
                return false;
            }
        
            public static void main(String[] args) {
                int[] nums = {3, 2, 1, 0, 4};
                System.out.println(canJump(nums));
            }
}
    
