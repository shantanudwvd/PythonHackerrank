from collections import Counter
size = int(input())
string = input()
myDict = dict(Counter(string))
print(myDict)
