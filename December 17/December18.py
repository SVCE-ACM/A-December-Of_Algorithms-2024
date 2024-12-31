def max_palindromic_profit(chain):
    gem_values = {'D': 500, 'R': 250, 'E': 100}
    n = len(chain)
    max_profit = 0

    def is_palindrome(sub):
        return sub == sub[::-1]

    for i in range(n):
        for j in range(i, n):
            substring = chain[i:j + 1]
            if is_palindrome(substring):
                substring_value = sum(gem_values[gem] for gem in substring)
                profit = substring_value * len(substring)
                max_profit = max(max_profit, profit)

    return max_profit

chain = input()
print(f"Maximum Profit: ${max_palindromic_profit(chain)}")
