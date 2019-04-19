string = input("Enter the string: ")
sub_string = input("Enter sub string: ")
count = 0
idx = 0
while string.count(sub_string, idx) != 0:
    count += 1
    idx = string.index(sub_string, idx)
    idx += 1
    if string.count(sub_string, idx) == 0:
        print(count)
        break

