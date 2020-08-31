string = input()
i = 0
max = 0
ct = 0
while i < len(string):
    if string[i] == 'A':
        ct += 1
        if i == len(string) - 1:
            if ct > max:
                max = ct
    elif string[i] != 'A':
        if ct > max:
            max = ct
        ct = 0
    i += 1
print(max)
