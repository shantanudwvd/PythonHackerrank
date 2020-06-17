def print_rangoli(size):
    row = 2 * size - 1
    column = 4 * size - 3
    my_list = []
    for idx in range(97, 97 + size):
        my_list.append(chr(idx))
    k = 1
    while k <= row:
        l = 1
        idx = len(my_list) - 1
        while l <= column:
            if l > size:
                idx = 0
                idx += 1
            elif l % 2 != 0 and l <= size:
                print(my_list[idx], end=" ")
                idx -= 1
            else:
                print("-", end="")
            l += 1
        print()
        k += 1


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
