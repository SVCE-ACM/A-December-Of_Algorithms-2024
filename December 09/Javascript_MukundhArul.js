function countCustomersWithOneReturn(returns) {
    return returns.filter(value => value === 1).length;
}

console.log(countCustomersWithOneReturn([1, 2, 1, 3, 1])); 
