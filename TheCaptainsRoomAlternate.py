k = int(input())
my_set = list(map(int, input().split()))
str_of_set = str(my_set)
my_set = set(my_set)
my_set = list(my_set)
for i in my_set:
    if str_of_set.count(str(i)) == 1:
        print(i)
        break
