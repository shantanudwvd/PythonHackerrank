def fibonacciModified(array, n):
    for i in range(0, n):
        array.append(array[i] + (array[i + 1] * array[i + 1]))
    return array[n - 1]


array = []
t1, t2, n = map(int, input().split())
array.append(t1)
array.append(t2)
result = fibonacciModified(array, n)
print(result)
