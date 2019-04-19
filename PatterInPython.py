size = int(input("Enter the size: "))
for i in range(size):
    for j in range(size):
        print(chr(64 + size - i), end="")
    print()
