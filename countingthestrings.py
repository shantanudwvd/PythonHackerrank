def solve():
    A = [5, 16, 2, 13, 5, 3, 4, 3, 14, 5]
    maxi = 0
    count = 0
    idx = 0
    for i in A:
        B = A[(idx + 1):]
        for j in B:
            if (i % 2 == 0 and j % 2 != 0) and i < j:
                i = j
                count += 1
            elif (i % 2 != 0 and j % 2 == 0) and i < j:
                i = j
                count += 1
        if count > maxi:
            maxi = count
        idx += 1
    return maxi

print(solve())
# N = int(input())
# A = map(int, input().split())
# output = solve(A)
# print(output)
