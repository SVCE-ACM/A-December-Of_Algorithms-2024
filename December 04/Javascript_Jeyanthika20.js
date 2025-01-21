function plantGrowthTracker(n) {
    if (n === 1 || n === 2) return 1;

    let prev = 1, curr = 1;
    for (let i = 3; i <= n; i++) {
        [prev, curr] = [curr, prev + curr];
    }
    return curr;
}

console.log(plantGrowthTracker(10)); 
console.log(plantGrowthTracker(12)); 
