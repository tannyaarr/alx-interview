#!/usr/bin/python3
"""Ä pile of coins of different values, determines the fewest number of coins
needed to meet a given total"""


def makeChange(coins, total):
    """making change"""
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for i in range(1, total + 1):

        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1