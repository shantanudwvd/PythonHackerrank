k = int(input())
room = list(map(int, input().split()))
my_list = room
my_list = str(my_list)
room = set(room)
room = list(room)
length = len(room)
length = length//k
temp = ""
i = 0
while i < len(room):
    if my_list.count(str(room[i])) == 1:
        print(room[i])
        break
    i += 1

