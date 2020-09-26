def pairInSortedRotated(array, n, x):
    global i
    for i in range(0, n - 1):
        if array[i] > array[i + 1]:
            break
    l = (i + 1) % n
    r = i
    while l != r:
        if array[l] + array[r] == x:
            return True
        if array[l] + array[r] < x:
            l = (l + 1) % n
        else:
            r = (n + r - 1) % n
    return False


array = list(map(int, input().split(" ")))
sum = 16
n = len(array)
if pairInSortedRotated(array, n, sum):
    print("array has two elements with sum 16")
else:
    print("array doesn't have two elements with sum 16 ")
