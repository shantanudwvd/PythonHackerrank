heapsize = 0
minh = 0
maxh = 0


def max_heapify(max_heap, i):
    left = 2 * i + 1
    right = 2 * i + 2
    if left < heapsize and max_heap[left] > max_heap[i]:
        largest = left
    else:
        largest = i
    if right < heapsize and max_heap[right] > max_heap[largest]:
        largest = right
    if largest != i:
        swap = max_heap[i]
        max_heap[i] = max_heap[largest]
        max_heap[largest] = swap
    max_heapify(max_heap, largest)


def min_heapify(min_heap, i):
    left = 2 * i + 1
    right = 2 * i + 2
    if left < heapsize and min_heap[left] < min_heap[i]:
        smallest = left
    else:
        smallest = i
    if right < heapsize and min_heap[right] < min_heap[smallest]:
        smallest = right
    if smallest != i:
        swap = min_heap[i]
        min_heap[i] = min_heap[smallest]
        min_heap[smallest] = swap
    min_heapify(min_heap, smallest)


def insert_valuein_max_heap(max_heap, length, val):
    max_heap[length] = val
    while length > 0 and max_heap[length // 2] < max_heap[length]:
        swap = max_heap[length // 2]
        max_heap[length // 2] = max_heap[length]
        max_heap[length] = swap
        length /= 2


def insert_valuein_min_heap(min_heap, length, val):
    min_heap[length] = val
    while length > 0 and min_heap[length // 2] > min_heap[length]:
        swap = min_heap[length // 2]
        min_heap[length // 2] = min_heap[length]
        min_heap[length] = swap
        length /= 2


def insert_element(max_heap, min_heap, val, size, maxh, minh):
    if val < max_heap[0]:
        maxh += 1
        insert_valuein_max_heap(max_heap, maxh, val)
    else:
        minh += 1
        insert_valuein_min_heap(min_heap, minh, val)
    if maxh == minh:
        return (max_heap[0] + min_heap[0]) / 2
    if maxh < minh:
        maxh += 1
        insert_valuein_max_heap(max_heap, maxh, min_heap[0])
        swap = min_heap[0]
        min_heap[0] = min_heap[minh]
        min_heap[minh] = swap
        minh -= 1
        heapsize = minh
        min_heapify(min_heap, 0)
    else:
        minh += 1
        insert_valuein_min_heap(min_heap, minh, max_heap[0])
        swap = max_heap[0]
        max_heap[0] = max_heap[maxh]
        max_heap[maxh] = swap
        maxh -= 1
        heapsize = maxh
        max_heapify(max_heap, 0)
    if size % 2 == 0:
        if maxh > minh:
            return max_heap[0]
        else:
            return min_heap[0]
    else:
        return (max_heap[0] + min_heap[0]) / 2


size = int(input())
max_heap = [0] * size
min_heap = [0] * size
a = int(input())
print(a)
b = int(input())
print((a + b) / 2)
if a < b:
    max_heap[0] = a
    min_heap[0] = b
else:
    min_heap[0] = a
    max_heap[0] = b
for i in range(2, size):
    x = int(input())
    insert_element(max_heap, min_heap, x, i, maxh, minh)
