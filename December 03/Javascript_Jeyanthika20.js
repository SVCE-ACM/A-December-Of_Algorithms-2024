function alternatingSquareArrangement(R, B) {
    if (Math.abs(R - B) > 1) return "Not possible";

    let result = [];
    let major = R >= B ? R : B;
    let minor = R >= B ? B : R;
    let majorColor = R >= B ? "R" : "B";
    let minorColor = R >= B ? "B" : "R";

    while (major > 0 || minor > 0) {
        if (major > 0) {
            result.push(majorColor);
            major--;
        }
        if (minor > 0 && (result.length === 0 || result[result.length - 1] === majorColor)) {
            result.push(minorColor);
            minor--;
        }
    }

    return result.join('');
}
console.log(alternatingSquareArrangement(3, 2)); 
console.log(alternatingSquareArrangement(4, 2)); 
