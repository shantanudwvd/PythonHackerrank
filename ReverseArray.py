def reverseArray(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start = start + 1
        end = end - 1


def rightRotate(arr, d, n):
    reverseArray(arr, 0, n - 1)
    reverseArray(arr, 0, d - 1)
    reverseArray(arr, d, n - 1)


def printArray(arr, size):
    for i in range(0, size):
        print(arr[i], end=' ')


arr = list(map(int, input().split(" ")))
n = len(arr)
k = 3
rightRotate(arr, k, n)
printArray(arr, n)
