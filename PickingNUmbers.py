from collections import Counter

size = int(input())
array = list(map(int, input().split()))
countDict = dict(Counter(array))
print(countDict)
keyArr = []
for k, v in countDict.items():
    keyArr.append(k)
keyArr = sorted(keyArr)
print(keyArr)
