queries = int(input())
my_list = []
for i in range(queries):
    my_list.append(input())
new_list = set(my_list)
new_list = list(new_list)
print(len(new_list))
for i in my_list:
    count = 0
    for j in new_list:
        if i in j:
            count += 1
    print(count, end=" ")
