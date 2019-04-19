size = int(input())
my_list = list(map(int, input().split(" ")))
pall =[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99]
print(all([True if i > 0 else False for i in my_list]) and any([True if i in pall else False for i in my_list]))

