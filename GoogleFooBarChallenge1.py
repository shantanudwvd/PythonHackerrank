my_list = list(map(int, input().split()))
new_list = []
occ = int(input())
temp = []
for i in range(0, len(my_list)):
    # print(my_list.count(my_list[i]))
    if my_list.count(my_list[i]) == occ and temp.count(my_list[i]) == 0:
        new_list.append(my_list[i])
    else:
        temp.append(my_list[i])
print(new_list)
my_set = set(my_list)
my_set = list(my_set)
print(my_list)
for i in my_set:
    print(f"Count of number {i} is: {my_list.count(i)}")
