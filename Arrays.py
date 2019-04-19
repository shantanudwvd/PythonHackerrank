import array
# size = int(input("Enter size: "))
value = array.array('i', map(int, input().split()))
value.reverse()
print(value)
for i in range(0, len(value)):
    print(value[i])
