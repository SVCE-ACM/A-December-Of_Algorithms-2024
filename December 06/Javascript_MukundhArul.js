function targetPairFinder(numbers, target) {
    let uniquePairs = [];
    let seen = new Set();

    for (let num of numbers) {
        const complement = target - num;
        if (seen.has(complement)) {
            uniquePairs.push([complement, num]);
        }
        seen.add(num);
    }

    return uniquePairs;
}

console.log(targetPairFinder([2, 4, 3, 7, 1, 5], 6)); 
console.log(targetPairFinder([10, 15, 3, 7, 8, 12, 5], 20));
