import Foundation

func groupPermutations(_ s: String) -> [Character: [String]] {
    let uniquePermutations = Set(permutations(s))
    var grouped = [Character: [String]]()
    
    for perm in uniquePermutations {
        if let firstChar = perm.first {
            grouped[firstChar, default: []].append(String(perm))
        }
    }
    
    return grouped
}

func permutations(_ s: String) -> [[Character]] {
    if s.count == 1 {
        return [[Character(s)]]
    }
    
    var result = [[Character]]()
    for (index, char) in s.enumerated() {
        var remaining = s
        remaining.remove(at: remaining.index(remaining.startIndex, offsetBy: index))
        let subPermutations = permutations(remaining)
        
        for subPerm in subPermutations {
            result.append([char] + subPerm)
        }
    }
    return result
}

// Example usage
let inputString = "abc"
let result = groupPermutations(inputString)
print(result)
