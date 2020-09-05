n, k = map(int, input().split())
myList = list(map(int, input().split()))
i = 0
X = 1
while True:
    myList = [(i-X) for i in myList]
    totSum = sum(myList)
    if totSum == k:
        print(X)
        break
    if totSum > k:
        print("-1")
        break
    else:
        i += 1
