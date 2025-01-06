def calculate_max_profit(gem_chain):
    gem_prices = {'D': 500, 'R': 250, 'E': 100}
    
    # Preprocess the string for Manacher's algorithm
    def preprocess(s):
        return '#' + '#'.join(s) + '#'
    
    # Manacher's algorithm to find the longest palindromic substring
    def manacher(s):
        T = preprocess(s)
        n = len(T)
        P = [0] * n
        C = R = 0
        
        for i in range(n):
            mirror = 2 * C - i
            if i < R:
                P[i] = min(R - i, P[mirror])
            while i + P[i] + 1 < n and i - P[i] - 1 >= 0 and T[i + P[i] + 1] == T[i - P[i] - 1]:
                P[i] += 1
            if i + P[i] > R:
                C, R = i, i + P[i]
        
        # Find the longest palindromic substring
        max_len = max(P)
        center_index = P.index(max_len)
        start = (center_index - max_len) // 2
        return gem_chain[start:start + max_len]
    
    # Get the longest palindromic substring
    longest_palindrome = manacher(gem_chain)
    
    # Calculate the total value of the longest palindromic substring
    total_value = sum(gem_prices[gem] for gem in longest_palindrome)
    
    # Calculate the profit
    profit = total_value * len(longest_palindrome)
    
    return profit

# Input from the user
gem_chain = input("Enter the gem chain: ")

# Output the maximum profit
print(f"Max profit: ${calculate_max_profit(gem_chain)}")
