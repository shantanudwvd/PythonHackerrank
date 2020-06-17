size = int(input())
prime = []
left = []
right = []
max = 0
for i in range(0, size):
    l, r = map(int, input().split(" "))
    if r > max:
        max = r
    left.append(l)
    right.append(r)
length = 0
for num in range(2, 50000):
    if all(num % i != 0 for i in range(2, num)):
        prime.append(num)
        length += 1
        if length == max:
            break
for i in range(0, size):
    sum = 0
    while left[i] <= right[i]:
        sum += prime[left[i]-1]
        left[i] += 1
    print(sum)
