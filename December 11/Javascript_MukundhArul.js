function robotReturnToOrigin(moves) {
    let x = 0, y = 0;
    for (const move of moves) {
        if (move === 'R') x++;
        else if (move === 'L') x--;
        else if (move === 'U') y++;
        else if (move === 'D') y--;
    }
    return x === 0 && y === 0;
}
console.log(robotReturnToOrigin("UDLR"));
