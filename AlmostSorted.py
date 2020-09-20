n = int(input())
array = list(map(int, input().split()))
srted = sorted(array)
if array == srted:
    print("Yes")
else:
    start = 0
    end = 0
    i = 0
    while i < len(array):
        if array[i] != srted[i] and start == 0:
            start = i
        elif array[i] != srted[i]:
            end = i
        i += 1
    temp = array[start]
    array[start] = array[end]
    array[end] = temp
    if array == srted:
        print("yes")
        print(f"swap {start+1} {end+1}")
    else:
        temp = array[start]
        array[start] = array[end]
        array[end] = temp
        if array[start:end+1][::-1] == srted[start:end+1]:
            print("yes")
            print(f"reverse {start+1} {end+1}")
        else:
            print("no")
