from collections import namedtuple
queries = int(input())
my_string = input()
mylist = []
j = 0
k = j
avg = 0
while j < len(my_string):
    temp = ""
    while k < len(my_string):
        if my_string[k] != " ":
            temp += my_string[k]
            k += 1
            j = k
        elif my_string[k] == " ":
            k += 1
            j = k
            break
    if temp != "":
        mylist.append(temp)
student = namedtuple('student', [mylist[0], mylist[1], mylist[2], mylist[3]])
l = 0
idx = 0
while l < len(mylist):
    if mylist[l] == "MARKS":
        idx = l
        break
    l += 1
for i in range(queries):
    my_string = input()
    my_list = []
    j = 0
    k = j
    while j < len(my_string):
        temp = ""
        while k < len(my_string):
            if my_string[k] != " ":
                temp += my_string[k]
                k += 1
                j = k
            elif my_string[k] == " ":
                k += 1
                j = k
                break
        if temp != "":
            my_list.append(temp)
    avg += int(my_list[idx])
    S = student(my_list[0], my_list[1], my_list[2], my_list[3])
print(avg/queries)
