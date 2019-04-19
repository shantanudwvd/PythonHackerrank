import math as m
no_of_lists, modulo = map(int, input().split())
my_list = []
new_list = []
for i in range(no_of_lists):
    my_list = list(map(int, input().split()))
    my_list.pop(0)
    new_list.append(m.pow(max(my_list), 2))
    my_list.clear()
if sum(new_list) < modulo:
    print(int(sum(new_list) % modulo))
else:
    print(modulo-1)
