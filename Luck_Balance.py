n, d = map(int, input().split())
myDict = []
luckBal = 0
for i in range(n):
    k, v = map(int, input().split())
    if v == 0:
        luckBal += k
    else:
        myDict.append(k)
for i in range(1, d + 1):
    if len(myDict) != 0:
        keyMax = max(myDict)
        luckBal += keyMax
        myDict.remove(keyMax)
print(luckBal - sum(myDict))
