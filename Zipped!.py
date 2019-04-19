size, queries = map(int, input().split())
pall = []
for i in range(queries):
    my_list = list(map(float, input().split()))
    pall.append(my_list)
new_list = list(zip(*pall))
for i in new_list:
    avg = sum(i)/queries
    print(avg)

