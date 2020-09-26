def pairsInSortedRotated(array, n, x):
    global i
    for i in range(n):
        if array[i] > array[i + 1]:
            break
    l = (i + 1) % n
    r = i
    cnt = 0
    while l != r:
        if array[l] + array[r] == x:
            cnt += 1
            if l == (r - 1 + n) % n:
                return cnt
            l = (l + 1) % n
            r = (r - 1 + n) % n
        elif array[l] + array[r] < x:
            l = (l + 1) % n
        else:
            r = (n + r - 1) % n
    return cnt


array = list(map(int, input().split(" ")))
s = 16
print(pairsInSortedRotated(array, 6, s))
