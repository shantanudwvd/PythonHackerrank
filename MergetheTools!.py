def merge_the_tools(my_string, k):
    n = len(my_string)
    t = n//k
    i = j = 0
    while i < t:
        sample = ""
        idx = 0
        while idx != n/t:
            sample += my_string[j]
            j += 1
            idx += 1
        temp = ""
        for k in sample:
            if k not in temp:
                temp += k
        print(temp)
        i += 1


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
