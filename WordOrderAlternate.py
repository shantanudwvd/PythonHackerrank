from collections import Counter
queries = int(input())
my_list = []
for i in range(queries):
    my_list.append(input())
my_dict = Counter(my_list)
print(len(my_dict))
for k, v in my_dict.items():
    print(f"{v}", end=" ")
