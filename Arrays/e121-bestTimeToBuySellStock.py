def maxProfit(prices):
    maxProfit=0
    currProfit=0
    slow,fast=0,1
    while slow < fast < len(prices):
        if prices[fast]-prices[slow] <= 0:
            slow=fast
        currProfit=max(currProfit, prices[fast]-prices[slow])
        maxProfit=max(maxProfit, currProfit)
        fast+=1
    return maxProfit

print(maxProfit([7,6,4,3,1]))