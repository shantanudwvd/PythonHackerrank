def reverse_of_list(my_list):
    i = 0
    new_list = []
    while i < len(my_list):
        new_list.append(my_list[i][::-1])
        i += 1
    print(new_list)


my_list = []
size = int(input("enter list size: "))
i = 0
while i < size:
    my_list.append(input())
    i += 1
reverse_of_list(my_list)
