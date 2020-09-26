def maxSum(array):
    arraySum = 0
    currVal = 0
    n = len(array)
    for i in range(0, n):
        arraySum = arraySum + array[i]
        currVal = currVal + (i * array[i])
    maxVal = currVal
    for j in range(1, n):
        currVal = currVal + arraySum - n * array[n - j]
        if currVal > maxVal:
            maxVal = currVal
    return maxVal


array = list(map(int, input().split(" ")))
print("Max sum is: ", maxSum(array))
