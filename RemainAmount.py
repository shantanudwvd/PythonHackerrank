def RemainAmount(n, target):
    if n == target:
        return "Yes"
    elif n < target:
        return "No"
    RemainAmount(n-3, target)
    RemainAmount(n-7, target)


cases = int(input())
for i in range(cases):
    target = int(input())
    RemainAmount(1000, target)
