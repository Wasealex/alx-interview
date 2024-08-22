#!/usr/bin/python3
"""a module for making change using the fewest coins possible
"""
def makeChange(coins, total):
    """
    determine the fewest number of coins to make up a total
    Args:
        coins: a list of the values of the coins in your possession
        total: the total amount for which you are making change
        Returns:
            the minimum number of coins needed to make up the total
            or -1 if it is not possible to create the total
    """
    if total <= 0:  # if total is 0 or less, no coins are needed
        return 0
    
    dp = [float('inf')] * (total + 1)  # initialize the dp list
    dp[0] = 0
    
    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:  # if the coin is less than the total
                dp[i] = min(dp[i], dp[i - coin] + 1)  # update the dp list
    
    if dp[total] == float('inf'):  # if no solution was found
        return -1
    
    return dp[total]
