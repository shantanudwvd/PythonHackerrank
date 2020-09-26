def preprocess(arr, n):
    temp = [None] * (2 * n)
    for i in range(n):
        temp[i] = temp[i + n] = arr[i]
    return temp


def leftRotate(arr, n, k, temp):
    start = k % n
    for i in range(start, start + n):
        print(temp[i], end=" ")
    print("")


arr = list(map(int, input().split(" ")))
n = len(arr)
temp = preprocess(arr, n)
k = 2
leftRotate(arr, n, k, temp)
k = 3
leftRotate(arr, n, k, temp)
k = 4
leftRotate(arr, n, k, temp)
