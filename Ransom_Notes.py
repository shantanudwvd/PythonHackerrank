from collections import Counter
n, m = map(int, input().split())
string1 = list(map(str, input().split()))
myDict1 = dict(Counter(string1))
string2 = list(map(str, input().split()))
myDict2 = dict(Counter(string2))
mySet = set(string2)
ct = 0
for i in mySet:
    if i in myDict1 and myDict2.get(i) <= myDict1.get(i):
        ct += 1
if ct == len(mySet):
    print("Yes")
else:
    print("No")
