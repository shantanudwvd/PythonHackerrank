def search(arr, l, h, key):
    if l > h:
        return -1
    mid = (l + h) // 2
    if arr[mid] == key:
        return mid
    if arr[l] <= arr[mid]:
        if arr[l] <= key <= arr[mid]:
            return search(arr, l, mid - 1, key)
        return search(arr, mid + 1, h, key)
    if arr[mid] <= key <= arr[h]:
        return search(arr, mid + 1, h, key)
    return search(arr, l, mid - 1, key)


arr = list(map(int, input().split(" ")))
key = 6
i = search(arr, 0, len(arr) - 1, key)
if i != -1:
    print("Index: % d" % i)
else:
    print("Key not found")
