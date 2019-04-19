def reverse(new_list):
    return[name[::-1] for name in new_list]


size = int(input("Enter the size: "))
my_list = []
for i in range(0, size):
    my_list.append(input("Enter string: "))
reverse(my_list)
