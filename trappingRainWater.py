heights = list(map(int, input().split(" ")))
print(heights)
val = int(input())
ct = 0
for i in heights:
    if i == val:
        print("It exists")
    else:
        ct += 1
if ct == 1:
    print("No it doesn't exist")
