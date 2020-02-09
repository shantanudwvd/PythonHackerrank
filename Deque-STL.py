def max_in_subarray(array, window_size, arr_size):
    for idx in range(0, arr_size - window_size + 1):
        max_ele = array[idx]
        for j in range(1, window_size):
            if array[idx + j] > max_ele:
                max_ele = array[idx + j]
        print(max_ele, end=" ")


queries = int(input("Enter queries: "))
print("Enter the array size and windows size: ")
length, k = map(int, input().split())
print("Enter elements: ")
arr = list(map(int, input().split()))
n = len(arr)
for i in range(0, queries):
    max_in_subarray(arr, k, n)
