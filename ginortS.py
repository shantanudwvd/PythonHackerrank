my_string = input()
lower = ""
upper = ""
odd = ""
even = ""
for i in my_string:
    if i.islower():
        lower += i
    elif i.isupper():
        upper += i
    elif i.isdigit():
        if int(i) % 2 != 0:
            odd += i
        else:
            even += i
for i in sorted(lower):
    print(i, end="")
for i in sorted(upper):
    print(i, end="")
for i in sorted(odd):
    print(i, end="")
for i in sorted(even):
    print(i, end="")
