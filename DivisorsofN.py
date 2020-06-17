t = int(input())
for i in range(t):
    count = 0
    val = int(input())
    for i in range(2, val):
        if val % i == 0 and i % 2 == 0:
            count += 1
    print(count)