from collections import Counter
t = int(input())
for i in range(t):
    size = int(input())
    array = list(map(int, input().split()))
    if size == 1:
        print("-1")
    else:
        heights = sorted(Counter(array).items())
        for idx in heights:
            array.append(idx[1])
        for idx in array:
            print(idx)
    array.clear()
