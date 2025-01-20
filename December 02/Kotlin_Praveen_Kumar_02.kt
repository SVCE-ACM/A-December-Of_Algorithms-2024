fun waveSort(arr: MutableList<Int>): List<Int> {
    arr.sort()
    for (i in 0 until arr.size - 1 step 2) {
        val temp = arr[i]
        arr[i] = arr[i + 1]
        arr[i + 1] = temp
    }
    return arr
}
