numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"
ct = 0
n = int(input())
password = input()
for idx in password:
    if idx in numbers:
        ct += 1
        break
for idx in password:
    if idx in lower_case:
        ct += 1
        break
for idx in password:
    if idx in upper_case:
        ct += 1
        break
for idx in password:
    if idx in special_characters:
        ct += 1
        break
if 4-ct+len(password) < 6:
    print(4 - ct + 6 - (4-ct+len(password)))
else:
    print(4-ct)
