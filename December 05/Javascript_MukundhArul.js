function josephus(n, k) {
    let safePosition = 0;
    for (let i = 1; i <= n; i++) {
        safePosition = (safePosition + k) % i;
    }
    return safePosition + 1;
}
console.log(josephus(3, 2)); 
console.log(josephus(5, 3)); 
