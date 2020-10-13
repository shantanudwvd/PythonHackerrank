from collections import Counter

string = input()
validString = dict(Counter(string))
ctList = []
for v in validString.values():
    ctList.append(v)
charDict = dict(Counter(ctList))
if len(charDict) == 1:
    print("YES")
elif len(charDict) > 2:
    print("NO")
else:
    if list(charDict.values())[0] == 1:
        if int(list(charDict)[0]) - 1 == int(list(charDict)[1]) or int(list(charDict)[0]) - 1 == 0:
            print("YES")
        else:
            print("NO")
    elif list(charDict.values())[1] == 1:
        if int(list(charDict)[1]) - 1 == int(list(charDict)[0]) or int(list(charDict)[1]) - 1 == 0:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
