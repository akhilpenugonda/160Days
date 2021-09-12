def nonConstructibleChange(coins):
    coins.sort()
    currentCoinChange = 0
    for coin in coins:
        if(coin > currentCoinChange + 1):
            return currentCoinChange + 1
        else:
            currentCoinChange += coin
    return currentCoinChange + 1
