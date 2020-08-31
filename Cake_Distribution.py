n, k = map(int, input().split())
for i in range(k, 0, -1):
    if i == 1:
        print("No")
        break
    elif n % i == 0:
        print("Yes")
        break
