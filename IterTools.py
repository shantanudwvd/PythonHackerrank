# def even(a):
#     return a % 2 == 0
#
#
# number = list(map(int, input().split()))
# even = tuple(filter(even, number))
# # even = list(filter(even, number))
# print(even)
#############################################################
# number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# evens = list(filter(lambda a: a % 2 != 0, number))
# print(evens)
# evens = list(filter(lambda a: a % 2 == 0, number))
# print(evens)
#############################################################
# number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_list = [i for i in number if i % 2 == 0]
# print(even_list)
# even_list = [i for i in number if i % 2 != 0]
# print(even_list)
#############################################################
# number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new_iter = iter(number)
# for i in number:
#     print(next(new_iter), end=" ")
from Graphics import *
root = Tk()
w = Label(root, text='GeeksForGeeks.org!')
w.pack()
root.mainloop()