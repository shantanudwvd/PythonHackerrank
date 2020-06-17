size = int(input())
array = list(map(int, input().split()))
i = 0
while i < len(array):
    print(array[i] * array[i+1], end=" ")
    i += 2
