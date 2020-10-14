from collections import Counter

size = int(input())
array = list(map(int, input().split()))
ctrArr = dict(Counter(array))
maxVal = max(ctrArr.values())
print(size - maxVal)
