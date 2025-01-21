function minSwaps(nums) {
    const sorted = [...nums].sort((a, b) => a - b);
    const pos = {};
    sorted.forEach((num, i) => (pos[num] = i));
    let swaps = 0;

    for (let i = 0; i < nums.length; i++) {
        while (pos[nums[i]] !== i) {
            swaps++;
            const swapIdx = pos[nums[i]];
            [nums[i], nums[swapIdx]] = [nums[swapIdx], nums[i]];
        }
    }
    return swaps;
}
console.log(minSwaps([4, 3, 2, 1])); 
