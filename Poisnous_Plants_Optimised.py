def poisonousPlants(p):
    global_max = 0
    arr = []

    for i in range(0, len(p)):
        current_max = 0
        while len(arr) and arr[-1][0] >= p[i]:
            current_max = arr[-1][1]
            arr.pop()
        if len(arr) == 0:
            arr.append([p[i], 0])
        else:
            current_max += 1
            arr.append([p[i], current_max])
        global_max = max(global_max, current_max)
    return global_max


size = int(input())
array = list(map(int, input().split()))
print(poisonousPlants(array))
