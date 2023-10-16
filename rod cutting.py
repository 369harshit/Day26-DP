def rodCutting(price, n):
    # Initialize an array to store the maximum value for each length
    dp = [0] * (n + 1)

    # Fill the dp array using bottom-up dynamic programming
    for i in range(1, n + 1):
        max_val = float('-inf')
        for j in range(1, i + 1):
            max_val = max(max_val, price[j - 1] + dp[i - j])
        dp[i] = max_val

    return dp[n]

# Example usage:
price = [2,5,7,8,10]
length = 5

result = rodCutting(price, length)
print("Maximum value:", result)
