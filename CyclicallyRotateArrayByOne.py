def rotate(array, n):
    x = array[n - 1]
    for i in range(n - 1, 0, -1):
        array[i] = array[i - 1]
    array[0] = x


array = list(map(int, input().split()))
n = len(array)
print("Given arrayay is")
for i in range(0, n):
    print(array[i], end=' ')
rotate(array, n)
print("\nRotated arrayay is")
for i in range(0, n):
    print(array[i], end=' ')