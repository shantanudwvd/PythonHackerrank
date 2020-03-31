import math as m

queries = int(input())
for i in range(queries):
    size, x = map(int, input().split())
    array = list(map(int, input().split()))
    array.sort()
    if size % 2 == 0:
        median = (array[int(size/2) - 1] + array[int(size/2)]) / 2
    else:
        median = array[int(size/2)]
    print(abs(int(size/2) - array.index(x)))

