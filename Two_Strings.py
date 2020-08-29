cases = int(input())
for i in range(cases):
    str1 = input()
    str2 = input()
    my_set1 = set(str1)
    my_set2 = set(str2)
    ct = 0
    if len(my_set1) < len(my_set2):
        for i in my_set1:
            if i in my_set2:
                ct += 1
                break
        if ct == 1:
            print("YES")
        else:
            print("NO")
    else:
        for i in my_set2:
            if i in my_set1:
                ct += 1
                break
        if ct == 1:
            print("YES")
        else:
            print("NO")