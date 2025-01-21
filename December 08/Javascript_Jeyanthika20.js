function digitSquareSum(N) {
    function digitSquareSumOfNumber(num) {
        let total = 0;
        while (num > 0) {
            const digit = num % 10;
            total += digit * digit;
            num = Math.floor(num / 10);
        }
        return total;
    }

    let totalSum = 0;
    for (let i = 1; i <= N; i++) {
        totalSum += digitSquareSumOfNumber(i);
    }
    return totalSum;
}
console.log(digitSquareSum(10)); 
