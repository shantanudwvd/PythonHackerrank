def search(array, l, h, key):
    if l > h:
        return -1
    mid = (l + h) // 2
    if array[mid] == key:
        return mid
    if array[l] <= array[mid]:
        if array[l] <= key <= array[mid]:
            return search(array, l, mid - 1, key)
        return search(array, mid + 1, h, key)
    if array[mid] <= key <= array[h]:
        return search(array, mid + 1, h, key)
    return search(array, l, mid - 1, key)


array = list(map(int, input().split(" ")))
key = 6
i = search(array, 0, len(array) - 1, key)
if i != -1:
    print("Index: % d" % i)
else:
    print("Key not found")
