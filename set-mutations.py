size = int(input())
mylist = set(map(int,input().split()))
queries = int(input())
i=0
while i < queries:
    string = input()
    if "intersection_update" in string:
        idx = string.index(" ")
        idx += 1
        num = ""
        while idx < len(string):
            num = num + string[idx]
            idx += 1
        num = int(num)
        newlist = set(map(int,input().split()))
        mylist.intersection_update(newlist)
    elif "symmetric_difference_update" in string:
        idx = string.index(" ")
        idx += 1
        num = ""
        while idx < len(string):
            num = num + string[idx]
            idx += 1
        num = int(num)
        newlist = set(map(int, input().split()))
        mylist.symmetric_difference_update(newlist)
    elif "difference_update" in string:
        idx = string.index(" ")
        idx += 1
        num = ""
        while idx < len(string):
            num = num + string[idx]
            idx += 1
        num = int(num)
        newlist = set(map(int, input().split()))
        mylist.difference_update(newlist)
    elif "update" in string:
        idx = string.index(" ")
        idx += 1
        num = ""
        while idx < len(string):
            num = num + string[idx]
            idx += 1
        num = int(num)
        newlist = set(map(int,input().split()))
        mylist.update(newlist)
    i+=1
print(sum(mylist))