def change(amount, coins):
    # Initialize an array to store the number of combinations for each amount
    dp = [0] * (amount + 1)
    
    # There is one way to make change for amount 0: no coins
    dp[0] = 1
    
    # Iterate over each coin denomination
    for coin in coins:
        # Update dp array for each amount
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
    
    return dp[amount]

# Example usage:
amount = 15
coins = [2,3,5,10]

result = change(amount, coins)
print("Number of combinations:", result)