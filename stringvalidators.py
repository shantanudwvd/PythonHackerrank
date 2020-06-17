string = input()
i = 0
count = 0
while i < len(string):
    if string[i].isalnum():
        count += 1
        print("True")
        break
    i += 1
if count == 0:
    print("False")
i = 0
count = 0
while i < len(string):
    if string[i].isalpha():
        count += 1
        print("True")
        break
    i += 1
if count == 0:
    print("False")
i = 0
count = 0
while i < len(string):
    if string[i].isdigit() == True:
        count += 1
        print("True")
        break
    i += 1
if count == 0:
    print("False")
i = 0
count = 0
while i < len(string):
    if string[i].islower():
        count += 1
        print("True")
        break
    i += 1
if count == 0:
    print("False")
i = 0
count = 0
while i < len(string):
    if string[i].isupper():
        count += 1
        print("True")
        break
    i += 1
if count == 0:
    print("False")
