sizeofset = int(input())
myset = set(map(int,input().split()))
queries = int(input())
i = 0
while i < queries:
    string=input()
    if "remove" in string:
        idx = string.index(" ")
        idx += 1
        num = ""
        while idx < len(string):
            num = num + string[idx]
            idx += 1
        num = int(num)
        myset.remove(num)
    elif "discard" in string:
        idx = string.index(" ")
        idx += 1
        num = ""
        while idx < len(string):
            num = num + string[idx]
            idx += 1
        num = int(num)
        myset.discard(num)
    else:
        myset.pop()
    i+=1
myset=list(myset)
print(sum(myset))