def solve(A, B):
    temp = ""
    rem = ""
    ans = ""
    temp += A[0]
    l = 1
    while l < len(A):
        if A[l] not in temp:
            temp += A[l]
        else:
            rem += A[l]
            break
        l += 1
    i = 0
    ct = 0
    while i < len(A):
        if A[i] == rem:
            for j in range(i, B):
                if A[j] != rem:
                    ct = 1
                    break
            if ct == 1:
                for j in range(i, B):
                    ans += A[i]
        else:
            ans += A[i]
        i += 1
    return ans


string = input()
k = int(input())
print(solve(string, k))
# def sizeExpandArray(A):
#     i = 0
#     while i < len(A):
#         j = i + 1
#         while j < len(A):
#             a = A[i]
#             b = A[j]
#             if int(a / b) not in A:
#                 A.append(int(a / b))
#     return A
# list = [9,4]
# print(sizeExpandArray(list))