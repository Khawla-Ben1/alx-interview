#!/usr/bin/python3
"""
Change comes from within
"""


def makeChange(coins, total):
    """
    Calculate the fewest number of coins needed to meet the given amount total.

    Returns:
        int: Fewest number of coins needed to meet the total.
             -1 - If total cannot be met by any combination of coins you have.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    coin_count = 0
    for coin_value in coins:
        if coin_value <= total:
            coin_count += total // coin_value
            total %= coin_value
        if total == 0:
            break

    if total == 0:
        return coin_count
    else:
        return -1
