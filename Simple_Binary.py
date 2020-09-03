def subString(Str, n):
    myList = []
    for Len in range(1, n + 1):
        for i in range(n - Len + 1):
            j = i + Len - 1
            temp = ""
            for k in range(i, j + 1):
                temp += Str[k]
            myList.append(temp)
    myList.remove(Str)
    ct = 0
    for i in set(myList):
        if i.count("0") == i.count("1"):
            ct += 1
    print(ct)


size = int(input())
Str = input()
myList = list(Str)
temp = ""
for i in myList:
    if i != " ":
        temp += i
if len(temp) % 2 != 0:
    print("-1")
else:
    subString(temp, len(temp))
