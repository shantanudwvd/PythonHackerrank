def moveZerosToEnd(arr, n):
    count = 0
    for i in range(0, n):
        if arr[i] != 0:
            arr[count], arr[i] = arr[i], arr[count]
            count += 1


def printArray(arr, n):
    for i in range(0, n):
        print(arr[i], end=" ")


arr = list(map(int, input().split(" ")))
n = len(arr)
print("Original array:", end=" ")
printArray(arr, n)
moveZerosToEnd(arr, n)
print("\nModified array: ", end=" ")
printArray(arr, n)
