from collections import OrderedDict
items = int(input())
my_dict = OrderedDict()
digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
for i in range(items):
    my_string = input()
    temp = ""
    temp1 = ""
    for j in my_string:
        if j not in digits:
            temp += j
        else:
            temp1 += j
    item_name = temp
    net_price = int(temp1)
    total = 0
    for k, v in my_dict.items():
        if item_name == k:
            total = v
            break
    total += net_price
    my_dict[item_name] = total
for k, v in my_dict.items():
    print(f"{k}{v}")
