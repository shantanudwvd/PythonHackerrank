size = int(input("Enter the size of fibonacci list: "))
my_list = []
my_list.append(0)
my_list.append(1)
for i in range(2, size):
    my_list.append(my_list[i-2] + my_list[i-1])
print(my_list)
