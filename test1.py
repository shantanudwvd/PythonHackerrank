# array = list(map(int, input().split()))
# maxProfit = 0
# buy = 0
# buyidx = 0
# sell = 0
# sellidx = 0
# for i in range(len(array) - 1):
#     buy = array[i]
#     bidx = i
#     sell = max(array[i+1:])
#     sidx = array.index(sell)
#     profit = abs(sell - buy)
#     if profit > maxProfit:
#         maxProfit = profit
#         buyidx = bidx
#         sellidx = sidx
# print(f"Buy on - Day {buyidx+1} - Sell on - Day {sellidx+1} - Profit = {maxProfit}")

