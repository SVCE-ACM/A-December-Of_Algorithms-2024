let superEggDrop (k: int) (n: int) : int =
    let dp = Array.init (k + 1) (fun _ -> Array.create (n + 1) 0)
    let mutable moves = 0
    let mutable found = false

    while not found do
        moves <- moves + 1
        for eggs in 1 .. k do
            dp.[eggs].[moves] <- dp.[eggs - 1].[moves - 1] + dp.[eggs].[moves - 1] + 1
            if dp.[eggs].[moves] >= n then
                found <- true
    moves

// Example test cases
printfn "%d" (superEggDrop 2 6)  // Output: 3
printfn "%d" (superEggDrop 3 14) // Output: 4
