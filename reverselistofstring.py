def reverse_of_list(listofstrings):
    i = 0
    mylist = []
    while i < len(listofstrings):
        j = -1
        k = 0
        while k < len(listofstrings[i]):
            if (k == 0):
                revlist = ""
            revlist += (listofstrings[i][j])
            j -= 1
            k += 1
        mylist.append(revlist)
        i += 1
    print(mylist)


listofstrings = []
print("Enter list size: ")
size = int(input())
i = 0
while i < size:
    listofstrings.append(input())
    i += 1
reverse_of_list(listofstrings)
