def gem_value(gem):
    if gem == 'D':
        return 500
    elif gem == 'R':
        return 250
    elif gem == 'E':
        return 100
    else:
        return 0

def max_palindromic_chain_profit(chain):
    n = len(chain)
    if n == 0:
        return 0

    s = '@#' + '#'.join(chain) + '#$'
    p = [0] * len(s)
    c = r = 0

    for i in range(1, len(s) - 1):
        if i < r:
            p[i] = min(r - i, p[2 * c - i])
        while s[i + p[i] + 1] == s[i - p[i] - 1]:
            p[i] += 1
        if i + p[i] > r:
            c = i
            r = i + p[i]

    max_length = 0
    center = 0
    for i in range(1, len(s) - 1):
        if p[i] > max_length:
            max_length = p[i]
            center = i

    start = (center - max_length) // 2
    end = (center + max_length) // 2

    total_value = sum(gem_value(chain[i]) for i in range(start, end))

    profit = total_value * (end - start + 1)

    return profit
