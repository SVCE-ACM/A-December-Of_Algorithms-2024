def manachers_algorithm(S):
    S1 = '#'.join('^{}$'.format(S))
    LPS = [0] * len(S1)
    center = right = 0

    for i in range(1, len(S1) - 1):
        mirror = 2 * center - i
        if i < right:
            LPS[i] = min(right - i, LPS[mirror])

        while S1[i + LPS[i] + 1] == S1[i - (LPS[i] + 1)]:
            LPS[i] += 1

        if i + LPS[i] > right:
            center = i
            right = i + LPS[i]

    max_len, centerIndex = max((j, i) for i, j in enumerate(LPS))
    start = (centerIndex - max_len) // 2
    end = (centerIndex + max_len) // 2
    return S[start:end]

def MaxPalindromicChainInc(chain):
    gem_values = {'D': 500, 'R': 250, 'E': 100}
    longest_palindrome = manachers_algorithm(chain)

    if not longest_palindrome:
        return 0
    
    print(f"Longest Plaindrome: {longest_palindrome}")

    gem_sum = 0
    for gem in longest_palindrome:
        gem_sum += gem_values[gem]

    profit = gem_sum * len(longest_palindrome)
    return profit

if __name__ == "__main__":
    chain = input("Enter Your Chain: ").strip()
    profit = MaxPalindromicChainInc(chain)
    print(f"Chain: {chain} -> Max Profit: ${profit}")

