def surfaceArea(array):
    top_bottom = 2 * W * H
    area = 0
    if H == 1:
        for i in range(0, W):
            area += array[0][i]
        area *= 2
        for i in range(1, W):
            area += abs(array[0][i] - array[0][i - 1])
        area += array[0][0]
        area += array[0][W - 1]
        area += top_bottom
        total_area = area
    elif W == 1:
        for i in range(0, H):
            area += array[i][0]
        area *= 2
        for i in range(1, H):
            area += abs(array[i][0] - array[i - 1][0])
        area += array[0][0]
        area += array[H - 1][0]
        area += top_bottom
        total_area = area
    else:
        for i in range(0, H):
            area += array[i][0]
            area += array[i][W - 1]
        for i in range(0, W):
            area += array[1][i]
            area += array[H - 1][i]
        for i in range(0, W):
            for j in range(1, H):
                area += abs(array[j][i] - array[j - 1][i])
        for i in range(0, H):
            for j in range(1, W):
                area += abs(array[i][j] - array[i][j - 1])
        total_area = area + top_bottom
    return total_area


HW = input().split()
H = int(HW[0])
W = int(HW[1])
A = []
for _ in range(H):
    A.append(list(map(int, input().rstrip().split())))
result = surfaceArea(A)
print(result)
