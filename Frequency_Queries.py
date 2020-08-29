from collections import Counter
cases = int(input())
myList = []
freqDict = Counter()
for i in range(cases):
    query, val = map(int, input().split())
    if query == 1:
        myList.append(val)
        temp = [val]
        freqDict.update(temp)
    elif query == 2:
        if val in myList:
            myList.remove(val)
            temp = [val]
            freqDict.subtract(temp)
    elif query == 3:
        if len(myList) != 0:
            ct = 0
            for k, v in freqDict.items():
                if v == val:
                    ct += 1
                    break
            if ct == 1:
                print("1")
            else:
                print("0")
        else:
            print("0")
