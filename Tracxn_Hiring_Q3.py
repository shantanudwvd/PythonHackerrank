array = list(map(int, input().split()))
idx = 0
maxProfit = 0
buyDate = 0
sellDate = 0
while idx < len(array) - 1:
    buy = array[idx]
    i = array.index(max(array[idx:]))
    sell = array[i]
    if abs(sell-buy) > maxProfit:
        maxProfit = abs(sell-buy)
        buyDate = idx
        sellDate = i
    idx += 1
print(f"Buy on - Day {buyDate+1} - Sell on - Day {sellDate+1} - Profit = {maxProfit}")