package main

import "fmt"

func minSwaps(nums []int) int {
    // Create a map to store the position of each element in the sorted array
    pos := make(map[int]int)
    sortedNums := make([]int, len(nums))
    copy(sortedNums, nums)
    sort.Ints(sortedNums)

    for i, num := range sortedNums {
        pos[num] = i
    }

    count := 0
    for i := 0; i < len(nums); i++ {
        if pos[nums[i]] != i {
            count++
            temp := nums[i]
            nums[i] = nums[pos[nums[i]]]
            nums[pos[nums[i]]] = temp
            pos[nums[i]] = i
        }
    }
    return count
}

func main() {
    nums := []int{4, 3, 2, 1}
    fmt.Println(minSwaps(nums)) // Output: 2
}
