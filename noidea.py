n, m = map(int, input().split())
happiness = 0
array = list(map(int, input().split()))
setA = list(map(int, input().split()))
setB = list(map(int, input().split()))
string = {}
i = 0
while i < len(array):
    j = 0
    while j < len(setA):
        if array[i] == setA[j]:
            happiness += 1
        j += 1
    k = 0
    while k < len(setB):
        if array[i] == setB[k]:
            happiness -= 1
        k += 1
    i += 1
print(happiness)
