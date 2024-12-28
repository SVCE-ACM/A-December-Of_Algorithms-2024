int trapRainWater(List<int> height) {
  if (height.isEmpty) {
    return 0;
  }

  int left = 0, right = height.length - 1;
  int leftMax = 0, rightMax = 0;
  int trappedWater = 0;

  while (left < right) {
    if (height[left] < height[right]) {
      if (height[left] >= leftMax) {
        leftMax = height[left];
      } else {
        trappedWater += leftMax - height[left];
      }
      left++;
    } else {
      if (height[right] >= rightMax) {
        rightMax = height[right];
      } else {
        trappedWater += rightMax - height[right];
      }
      right--;
    }
  }

  return trappedWater;
}

void main() {
  List<int> height1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1];
  List<int> height2 = [4, 2, 0, 3, 2, 5];
  
  print(trapRainWater(height1)); // Output: 6
  print(trapRainWater(height2)); // Output: 9
}
