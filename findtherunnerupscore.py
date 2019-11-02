mylist = []
size = int(input("Enter the size of list: "))
i = 1
mylist = list(map(int, input("Enter numbers: ").split(" ")))
j = 0
while j < size:
    k = 0
    l = k + 1
    while l < size:
        if mylist[k] > mylist[l]:
            temp = mylist[k]
            mylist[k] = mylist[l]
            mylist[l] = temp
        k += 1
        l += 1
    j += 1
i = size - 1
while i >= 0:
    x = mylist[i]
    if mylist[i - 1] != x:
        print(mylist[i - 1])
        break
    i -= 1
