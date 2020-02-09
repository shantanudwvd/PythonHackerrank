size = int(input())
array = list(map(int, input().split(" ")))
dis_arr = set(array)
count = []
for i in dis_arr:
    count.append(array.count(i))
idx = 0
maximum = []
for i in dis_arr:
    add = 0
    if i + 2 in dis_arr:
        add += count[idx] + array.count(i + 2)
        maximum.append(add)
    else:
        add += count[idx]
        maximum.append(add)
for i in dis_arr:
    sub = 0
    if i - 2 in dis_arr:
        sub += count[idx] + array.count(i + 2)
        maximum.append(sub)
    else:
        sub += count[idx]
        maximum.append(sub)
print(max(maximum))
