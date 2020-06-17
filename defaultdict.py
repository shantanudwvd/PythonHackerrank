import collections
n, m = map(int, input().split())
word_groupA = []
for i in range(n):
    word_groupA.append(input())
word_groupB = []
for i in range(m):
    word_groupB.append(input())
for i in word_groupB:
    k = 1
    count = 0
    for j in word_groupA:
        if i == j:
            print(k, end=" ")
            count += 1
        k += 1
    if count == 0:
        print(-1)
    else:
        print()