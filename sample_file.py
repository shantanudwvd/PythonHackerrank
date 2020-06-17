size1 = int(input())
dictionary = []
for i in range(size1):
    var1 = input()
    dictionary.append(var1)
query = []
size2 = int(input())
for i in range(size2):
    var2 = input()
    query.append(var2)
final = 0
for i in query:
    count = 0
    for j in dictionary:
        for idx in i:
            if idx in j:
                count += 1