n, m = map(int, input().split())
happiness = 0
array = list(map(int, input().split()))
setA = set(map(int, input().split()))
setB = set(map(int, input().split()))
add = (setA.intersection(array))
sub = setB.intersection(array)
array = str(array)
plus = minus = 0
for i in add:
    plus += array.count(str(i))
for i in sub:
    minus += array.count(str(i))
print(happiness + plus - minus)
