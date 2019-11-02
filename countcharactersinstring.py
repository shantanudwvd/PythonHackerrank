name = input("Enter a string: ")
i = 0
list = []
i = 0
while i < len(name):
    char = name[i]
    if name.count(char) <= 1:
        print(char, end=" ")
        print(name.count(char), end="\n")
        i += 1
    elif name.count(char) > 1 and i == 0:
        list.append(char)
        print(char, end=" ")
        print(name.count(char), end="\n")
        i += 1
    else:
        if char in list:
            i += 1
        else:
            list.append(char)
            print(char, end=" ")
            print(name.count(char), end="\n")
            i += 1
