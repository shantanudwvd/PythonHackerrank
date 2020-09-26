from collections import Counter
size = int(input())
string = input()
myDict = dict(Counter(string))
for k, v in myDict.items():
    print(f"key is: {k} and value is: {v}")
print(myDict)
