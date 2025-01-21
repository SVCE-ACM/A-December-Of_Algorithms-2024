function waveSort(arr) {
    arr.sort((a, b) => a - b);
    for (let i = 0; i < arr.length - 1; i += 2) {
        [arr[i], arr[i + 1]] = [arr[i + 1], arr[i]];
    }
    return arr;
}
console.log(waveSort([10, 5, 6, 3, 2, 20, 100, 80])); 
console.log(waveSort([1, 2, 3, 4, 5, 6]));           
