size = int(input("Enter the size of the array: "))
print("Enter the elements of the array:", end="\n")
stock = list(map(int, input().split(" ")))
profit = 0
i = 0
while i+2 <= size:
    if stock[i] < stock[i+1] and stock[i+1] > stock[i+2]:
        profit += int(stock[i+1] - stock[i])
        i += 2
    elif profit == 0 and i == size:
        profit += (stock[size] - stock[i])
    else:
        i += 1
print(profit)
