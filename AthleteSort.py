n, m = map(int, input().split(" "))
my_list = []
temp = []
for i in range(n):
    temp = list(map(int, input().split(" ")))
    my_list.append(temp)
k = int(input())
new = list(zip(my_list))
for i in range(n):
    print(list(*new[i]))
