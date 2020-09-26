def leftRotate(arr, d, n):
    for i in range(d):
        leftRotatebyOne(arr, n)


def leftRotatebyOne(arr, n):
    temp = arr[0]
    for i in range(n - 1):
        arr[i] = arr[i + 1]
    arr[n - 1] = temp


def printArray(arr, size):
    for i in range(size):
        print("% d" % arr[i], end=" ")


arr = list(map(int, input().split(" ")))
leftRotate(arr, 2, 7)
printArray(arr, 7)
