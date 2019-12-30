# def reverse(new_list):
#     return[name[::-1].title() for name in new_list]
# size = int(input("Enter the size: "))
# string = []
# for i in range(1, size+1):
#     string.append(input())
# print(reverse(string))
# def func(l, **kwargs):
#     if kwargs.get('reverse_str') == True:
#         return[name[::-1].title() for name in l]
#     else:
#         return[name[::-1] for name in l]
# names = ["nitin","Solitaire","Infosys"]
# print(func(names,reverse_str = True))
def func(l, **kwargs):
    if kwargs.get('reverse_str'):
        nums = [name[::-1].title() for name in l]
    else:
        nums = [name[::-1] for name in l]


names = ("nitin","Solitaire","Infosys")
# names=list(names)
print(func(names, reverse_str=True))
