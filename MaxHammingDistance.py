def maxHamming(array, n):
    brr = [0] * (2 * n + 1)
    for i in range(n):
        brr[i] = array[i]
    for i in range(n):
        brr[n + i] = array[i]
    maxHam = 0
    for i in range(1, n):
        currHam = 0
        k = 0
        for j in range(i, i + n):
            if brr[j] != array[k]:
                currHam += 1
                k = k + 1
        if currHam == n:
            return n
        maxHam = max(maxHam, currHam)
    return maxHam


array = list(map(int, input().split(" ")))
n = len(array)
print(maxHamming(array, n))
