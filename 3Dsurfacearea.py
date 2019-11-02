def surfaceArea(A):
    top_bottom = 2 * W * H
    total_area = 0
    area = 0
    if H == 1:
        for i in range(0, W):
            area += A[0][i]
        area *= 2
        for i in range(1, W):
            area += abs(A[0][i] - A[0][i - 1])
        area += A[0][0]
        area += A[0][W - 1]
        area += top_bottom
        total_area = area
    elif W == 1:
        for i in range(0, H):
            area += A[i][0]
        area *= 2
        for i in range(1, H):
            area += abs(A[i][0] - A[i - 1][0])
        area += A[0][0]
        area += A[H - 1][0]
        area += top_bottom
        total_area = area
    else:
        for i in range(0, H):
            area += A[i][0]
            area += A[i][W - 1]
        for i in range(0, W):
            area += A[1][i]
            area += A[H - 1][i]
        for i in range(0, W):
            for j in range(1, H):
                area += abs(A[j][i] - A[j - 1][i])
        for i in range(0, H):
            for j in range(1, W):
                area += abs(A[i][j] - A[i][j - 1])
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
