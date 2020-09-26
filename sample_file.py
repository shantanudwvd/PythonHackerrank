def equalStacks(h1, h2, h3):
    sumh1 = sum(h1)
    sumh2 = sum(h2)
    sumh3 = sum(h3)
    lst = [sumh1, sumh2, sumh3]
    arr = [h1, h2, h3]
    while lst[0] != lst[1] or lst[1] != lst[2]:
        if sumh1 == sumh2 and sumh2 == sumh3:
            print(sumh1)
            break
        elif lst[0] == 0 or lst[1] == 0 or lst[2] == 0:
            return 0
        print("**")
        print(lst)
        print(arr)
        maxSumStack = max(lst)
        index = lst.index(maxSumStack)
        val = arr[index].pop(0)
        print(val)
        lst[index] = lst[index] - val
    return lst[0]


first_multiple_input = input().rstrip().split()
n1 = int(first_multiple_input[0])
n2 = int(first_multiple_input[1])
n3 = int(first_multiple_input[2])
h1 = list(map(int, input().rstrip().split()))
h2 = list(map(int, input().rstrip().split()))
h3 = list(map(int, input().rstrip().split()))
result = equalStacks(h1, h2, h3)
print(result)

