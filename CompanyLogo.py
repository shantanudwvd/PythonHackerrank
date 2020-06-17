from collections import Counter


def company_logo(string):
    my_list = []
    for i in string:
        my_list.append(i)
    my_dict = Counter(my_list)
    my_keys = list(my_dict.keys())
    my_val = list(my_dict.values())
    i = 0
    while i < 3:
        val = max(my_val)
        if my_val.count(val) > 1:
            temp = {}
            k = 0
            while k < len(my_val):
                if my_val[k] == val:
                    temp[my_keys[k]] = my_val[k]
                k += 1
            for char in sorted(temp.keys()):
                if i < 3:
                    print(f"{char} {val}")
                    my_val.remove(val)
                    my_keys.remove(char)
                    i += 1
            temp.clear()
        else:
            idx = my_val.index(max(my_val))
            my_val.pop(idx)
            print(my_keys[idx], end=" ")
            my_keys.pop(idx)
            print(val)
            i += 1


if __name__ == '__main__':
    s = input()
    company_logo(s)
