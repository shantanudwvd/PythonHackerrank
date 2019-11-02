list1 = []
list2 = []
common = []
print("enter the size of list 1: ")
size1 = int(input())
i = 0
while i < size1:
    list1.append(int(input()))
    i += 1
print("enter the size of list 2: ")
size2 = int(input())
i = 0
while i < size2:
    list2.append(int(input()))
    i += 1
i = 0
x = 0
while i < size1:
    j = 0
    while j < size2:
        if (list1[i] == list2[j]):
            common.append(list1[i])
            break
        else:
            j += 1
    i += 1
print(common)
