size = int(input())
tickets = []
for i in range(size):
    tickets.append(int(input()))
ticket = sorted(tickets)
maxCount = 1
ct = 1
i = 1
while i < size:
    if ticket[i] - ticket[i-1] == 1 or ticket[i] - ticket[i-1] == 0:
        ct += 1
        i += 1
    else:
        if ct > maxCount:
            maxCount = ct
        ct = 1
        i += 1
print(maxCount)
