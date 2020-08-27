n, p = map(int, input().split())
ct=0
for i in range(1, n+1):
    if i ** 2 % p == 1:
        ct += 1
print(ct)