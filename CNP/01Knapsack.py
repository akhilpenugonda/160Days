
from sys import stdin

def knapsack(weights, values, n, maxWeight, i) :
    if(i == n):
        return 0
    if(weights[i] > maxWeight):
        ans = knapsack(weights, values, n, maxWeight, i+1)
    else:
        #including the item
        ans1 = values[i] + knapsack(weights, values, n, maxWeight-weights[i], i+1)
        #excluding the item
        ans2 = knapsack(weights, values, n, maxWeight, i+1)
        ans = max(ans1, ans2)
    return ans
def knapsackiter(W, val, wts):
    n = len(val)
    dp = [[0 for j in range(W+1)] for i in range(n+1)]
    
def takeInput() :
    n = int(stdin.readline().rstrip())

    if n == 0 :
        return list(), list(), n, 0

    weights = list(map(int, stdin.readline().rstrip().split(" ")))
    values = list(map(int, stdin.readline().rstrip().split(" ")))
    maxWeight = int(stdin.readline().rstrip())

    return weights, values, n, maxWeight


#main
weights, values, n, maxWeight = takeInput()

print(knapsack(weights, values, n, maxWeight, 0))