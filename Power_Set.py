def Power_Set(string):
    my_set = []
    idx = 1
    for i in string:
        temp = i
        for j in string[idx:]:
            my_set.append(temp + j)
        idx += 1
    return my_set


string = input()
my_list = Power_Set(string)
for i in my_list:
    my_list.append(Power_Set(i))