size = int(input("Enter the size of fibonacci list: "))
myList = [0, 1]
for i in range(2, size):
    myList.append(myList[i-2] + myList[i-1])
print(myList)
