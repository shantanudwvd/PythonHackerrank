x = int(input())
y = int(input())
z = int(input())
n = int(input())
my_list = []
for i in range(0, x+1):
    for j in range(0, y+1):
        for k in range(0, z+1):
            if i+j+k != n:
                newlist = []
                newlist.append(i)
                newlist.append(j)
                newlist.append(k)
                my_list.append(newlist)
print(my_list)
