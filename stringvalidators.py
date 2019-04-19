string=input()
i = 0
count = 0
while i < len(string):
    if string[i].isalnum() == True:
        count += 1
        print("True")
        break
    i += 1
if (count == 0):
    print("False")
i = 0
count = 0
while i < len(string):
    if string[i].isalpha() == True:
        count += 1
        print("True")
        break
    i += 1
if (count == 0):
    print("False")
i = 0
count = 0
while i < len(string):
    if string[i].isdigit() == True:
        count += 1
        print("True")
        break
    i += 1
if (count == 0):
    print("False")
i=0
count=0
while i<len(string):
    if string[i].islower()==True:
        count+=1
        print("True")
        break
    i+=1
if(count==0):
    print("False")
i=0
count=0
while i<len(string):
    if string[i].isupper()==True:
        count+=1
        print("True")
        break
    i+=1
if(count==0):
    print("False")