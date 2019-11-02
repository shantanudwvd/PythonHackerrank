my_setA = list(map(int, input().split()))
my_setB = my_setA
my_setB = str(my_setB)
queries = int(input())
ans = True
i = 0
while i < queries:
    subset = list(map(int, input().split()))
    j = 0
    count = 0
    while j < len(subset):
        if str(subset[j]) in my_setB:
            count += 1
        j += 1
    if count == len(subset) and len(my_setA) > len(subset):
        if not ans:
            subset.clear()
    else:
        ans = False
        subset.clear()
    i += 1
print(ans)
