size = int(input())
array = list(map(int, input().split()))
max = 0
i = 0
height = 0
while i < len(array):
    height = size * min(array[i:])
    if height > max:
        max = height
    size -= 1
    i += 1
print(max)
