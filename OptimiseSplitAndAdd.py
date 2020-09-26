def SplitAndAdd(A, length, rotation):
    tmp = [0 for i in range(length * 2)]
    for i in range(length):
        tmp[i] = A[i]
        tmp[i + length] = A[i]
    for i in range(rotation,
                   rotation + length, 1):
        A[i - rotation] = tmp[i]


array = list(map(int, input().split(" ")))
n = len(array)
position = 2
SplitAndAdd(array, n, position)
for i in range(n):
    print(array[i], end=" ")
print()
