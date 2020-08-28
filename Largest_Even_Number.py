number = input()
odd = number[len(number) - 1]
even = 0
idx = 0
i = 0
diff = 0
while i < len(number):
    if int(number[i]) % 2 == 0 and int(odd) - int(number[i]) > diff:
        idx = i
        even = number[i]
        diff = int(odd) - int(number[i])
    i += 1
for i in range(0, len(number)):
    if i == idx:
        print(odd, end="")
    elif i == len(number) - 1:
        print(even, end="")
    else:
        print(number[i], end="")
