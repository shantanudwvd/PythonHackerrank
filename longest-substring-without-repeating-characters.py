string = input()
temp = ""
substring = []
i = 0
print(string)
while i < len(string):
    if len(temp) == 0:
        temp += string[i]
        i += 1
    elif string[i] not in temp:
        temp += string[i]
        i += 1
    elif string[i] in temp:
        if len(substring) == 0:substring.append(temp)
        elif len(temp) > len(substring[0]):
            substring[0] = temp
        temp = ""

print(len(substring[0]))