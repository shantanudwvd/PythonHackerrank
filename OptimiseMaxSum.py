def maxSum(array, n):
    cum_sum = 0
    for i in range(0, n):
        cum_sum += array[i]
    curr_val = 0
    for i in range(0, n):
        curr_val += i * array[i]
    res = curr_val
    for i in range(1, n):
        next_val = (curr_val - (cum_sum - array[i - 1]) + array[i - 1] * (n - 1))
        curr_val = next_val
        res = max(res, next_val)
    return res


array = list(map(int, input().split(" ")))
n = len(array)
print(maxSum(array, n))
