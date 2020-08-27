n, m = map(int, input().split())
idx = 0
max = 0
for i in range(n):
    val = list(map(int, input().split()))
    str1 = ' '.join([str(i) for i in val])
    print(str1)
    ct = str1.count('1')
    if ct > max:
        max = ct
        idx = i
print(idx)

