def max_in_subarray(array, window_size, arr_size):
    for idx in range(0, arr_size - window_size + 1):
        max_ele = array[idx]
        for j in range(1, window_size):
            if array[idx + j] > max_ele:
                max_ele = array[idx + j]
        print(max_ele, end=" ")


queries = int(input())
for i in range(0, queries):
    n, k = map(int, input().split(" "))
    arr = list(map(int, input().split()))
    max_in_subarray(arr, k, n)
