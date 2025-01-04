//(26) Escape The Lava Field
#include <stdio.h>
#include <stdbool.h>

bool canJump(int* nums, int numsSize) {
    int maxReach = 0;
    for (int i = 0; i < numsSize; i++) {
        if (i > maxReach) {
            return false;
        }
        maxReach = (maxReach > i + nums[i]) ? maxReach : i + nums[i];
    }
    return true;
}

int main() {
    int nums1[] = {2, 3, 1, 0, 4};
    int nums2[] = {3, 2, 1, 0, 4};
    int size1 = sizeof(nums1) / sizeof(nums1[0]);
    int size2 = sizeof(nums2) / sizeof(nums2[0]);
    
    printf("%s\n", canJump(nums1, size1) ? "True" : "False");
    printf("%s\n", canJump(nums2, size2) ? "True" : "False");
    
    return 0;
}

