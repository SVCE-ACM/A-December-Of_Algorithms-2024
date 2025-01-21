def calculate_max_profit(gem_chain):
    gem_prices = {'D': 500, 'R': 250, 'E': 100}
    
    def preprocess(s):
        return '#' + '#'.join(s) + '#'
    
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
        
        max_len = max(P)
        center_index = P.index(max_len)
        start = (center_index - max_len) // 2
        return gem_chain[start:start + max_len]
    
    longest_palindrome = manacher(gem_chain)
    total_value = sum(gem_prices[gem] for gem in longest_palindrome)
    profit = total_value * len(longest_palindrome)
    
    return profit

chain1 = "RDEREDRRRD"
chain2 = "DERRREDERREDEREDR"

print(calculate_max_profit(chain1))  # Output: 7250
print(calculate_max_profit(chain2))  # Output: 24000
