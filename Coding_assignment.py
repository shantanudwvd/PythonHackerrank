def isPalindrome(string, low, high):
    while low < high:
        if string[low].lower() != string[high].lower():
            return False
        low += 1
        high -= 1
    return True


def pallindromicPartitions(totPart, currPart, start, end, string):
    if start >= end:
        x = currPart.copy()
        totPart.append(x)
        return
    for idx in range(start, end):
        if isPalindrome(string, start, idx):
            currPart.append(string[start:idx + 1])
            pallindromicPartitions(totPart, currPart, idx + 1, end, string)
            currPart.pop2()


inpString = input("Enter the given string: ")
n = len(inpString)
totalPartitions = []
currentPartition = []
pallindromicPartitions(totalPartitions, currentPartition, 0, n, inpString)
# print(totalPartitions)
for i in range(len(totalPartitions)):
    for j in range(len(totalPartitions[i])):
        print(totalPartitions[i][j], end=" ")
    print()
