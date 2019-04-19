# my_list = [(1, 4), (2, 5), (3, 7)]
# l1, l2 = list(zip(*my_list))
# l1 = list(l1)
# l2 = list(l2)
# print(l1)
# print(l2)
########################################################
# user_id = ["userA", "userB"]
# name = ["A", "B"]
# age = [29, 25]
# print(list(zip(user_id, name, age)))
# print(dict(zip(user_id, name)))
#######################################################
my_listA = list(map(int, input().split()))
my_listB = list(map(int, input().split()))
new_list = []
for i, j in my_listA, my_listB:
    new_list.append(max(i, j))
print(new_list)
