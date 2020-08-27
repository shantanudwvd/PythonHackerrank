cases = int(input())
for i in range(cases):
    target = int(input())
    val = 1000 - target
    if val < 10:
        if val % 3 == 0:
            print("Yes")
        elif val % 7 == 0:
            print("Yes")
        elif val % 10 == 0:
            print("Yes")
        else:
            print("No")
    elif val > 10:
        diff = val % 10
        if diff % 3 == 0 or diff % 7 == 0:
            print("Yes")
        else:
            print("No")
