import math


def Log2(x):
    if x == 0:
        return False
    return math.log10(x) / math.log10(2)


def isPowerOfTwo(n):
    return math.ceil(Log2(n)) == math.floor(Log2(n))


size = int(input())
myList = list(map(int, input()))
i = 0
ct = 0
while i < len(myList):
    j = i + 1
    while j < len(myList):
        if isPowerOfTwo(myList[i] & myList[j]):
            ct += 1
        j += 1
    i += 1
print(ct)
