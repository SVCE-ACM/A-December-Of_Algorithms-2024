//(27) Trapping Rain Water:
#include <stdio.h>

int trap(int* height, int heightSize) {
    if (heightSize == 0) return 0;
    
    int left[heightSize], right[heightSize];
    left[0] = height[0];
    right[heightSize - 1] = height[heightSize - 1];
    
    for (int i = 1; i < heightSize; i++) {
        left[i] = (left[i - 1] > height[i]) ? left[i - 1] : height[i];
    }
    
    for (int i = heightSize - 2; i >= 0; i--) {
        right[i] = (right[i + 1] > height[i]) ? right[i + 1] : height[i];
    }
    
    int totalWater = 0;
    for (int i = 0; i < heightSize; i++) {
        totalWater += (left[i] < right[i] ? left[i] : right[i]) - height[i];
    }
    
    return totalWater;
}

int main() {
    int height1[] = {0,1,0,2,1,0,1,3,2,1,2,1};
    int height2[] = {4,2,0,3,2,5};
    int size1 = sizeof(height1) / sizeof(height1[0]);
    int size2 = sizeof(height2) / sizeof(height2[0]);
    
    printf("%d\n", trap(height1, size1));
    printf("%d\n", trap(height2, size2));
    
    return 0;
}

