inpStr, flag = map(str, input().split())
if int(flag) == 1:
    print(inpStr[0::2])
elif int(flag) == 0:
    print(inpStr[1::2])