queries = int(input())
for i in range(queries):
    size, x = map(int, input().split())
    array = list(map(int, input().split()))
    array.sort()
    if size % 2 == 0:
        median = (array[int(size/2) - 1] + array[int(size/2)]) / 2
    else:
        median = array[int(size/2)]
    if size % 2 == 0:
        if x in array:
            print(abs(size - array.index(x) -1))
        else:
            print(1)
    # else:
    #     if x in array:
    #
    #     else:

# thing_index = thing_list.index(elem) if elem in thing_list else -1

