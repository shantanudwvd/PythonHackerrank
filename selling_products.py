n = int(input())
ids = list(map(int, input().split(" ")))
m = int(input())
for i in set(ids):
    count = ids.count(i)
    if count <= m:
        for j in range(0, count):
            ids.remove(i)
            m -= 1
print(len(set(ids)))
