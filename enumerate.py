def func(stringlist, string):
    count = 0
    for pos, name in enumerate(stringlist):
        if name == string:
            print(f"Position is: {pos}")
            count += 1
            break
    if count == 0:
        print("-1")


# stringlist = ["ab", "bc", "cd", "ef", "gh", "ij"]
stringlists = list(map(str, input().split()))
func(stringlists, input("Enter a string you want to find: "))
