cases = int(input())
for i in range(cases):
    size = int(input())
    array = list(map(int, input().split()))
    i = -1
    eq = 0
    j = 1
    rightadd = sum(array[j:])
    left = 0
    ans = 0
    while i < len(array):
        if left == rightadd:
            print("YES")
            ans += 1
            break
        else:
            eq += 1
            j += 1
            i += 1
            if i == size - 1:
                break
            left += array[i]
            rightadd -= array[eq]
    if ans == 0:
        print("NO")
    array.clear()
