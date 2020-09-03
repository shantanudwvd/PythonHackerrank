def find3Numbers(A, arr_size, threshold):
    ct = 0
    # Fix the first element as A[i]
    for i in range(0, arr_size - 2):
        # Fix the second element as A[j]
        for j in range(i + 1, arr_size - 1):
            # Now look for the third number
            for k in range(j + 1, arr_size):
                if abs(A[k] - A[i]) > threshold:
                    break
                elif abs(A[k] - A[i]) <= threshold:
                    ct += 1
                    print("Triplet is", A[i], ", ", A[j], ", ", A[k])
    print(ct)


n, d = map(int, input().split())
A = list(map(int, input().split()))
find3Numbers(A, len(A), d)
