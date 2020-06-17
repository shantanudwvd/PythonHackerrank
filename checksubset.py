queries = int(input())
for i in range(0, queries):
    count = 0
    SetA = []
    sizeofA = int(input())
    SetA = list(map(int, input().split(" ")))
    SetB = []
    sizeofB = int(input())
    SetB = list(map(int, input().split(" ")))
    j = 0
    while j < sizeofA:
        k = 0
        while k < sizeofB:
            if SetA[j] == SetB[k]:
                count += 1
                break
            k += 1
        j += 1
    if count == sizeofA:
        print("True")
    else:
        print("False")
