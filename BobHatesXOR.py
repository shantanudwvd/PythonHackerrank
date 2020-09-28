A = list(map(int, input().split()))
n = len(A)
B = int(input())
start = 0
end = start + B
ct = 0
for i in range(len(A)-B+1):
    test_list = A[start:end]
    cost = 999999
    XOR = 0
    print(test_list)
    for i in range(0, len(test_list)):
        XOR ^= test_list[i]
    for i in range(0, len(test_list)):
        if cost > abs((XOR ^ test_list[i]) - test_list[i]):
            cost = abs((XOR ^ test_list[i]) - test_list[i])
    ct += cost
    start += 1
    end = start + B
print(ct)
