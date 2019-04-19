string=input("Enter a string: ")
i=0
list=[]
while i<len(string):
    if string[i].isupper()==True:
        list.append(string[i].lower())
    elif string[i].islower()==True:
        list.append(string[i].upper())
    else:
        list.append(string[i])
    i+=1
print(list)
i=0
while i<len(list):
    print(list[i],end="")
    i+=1
