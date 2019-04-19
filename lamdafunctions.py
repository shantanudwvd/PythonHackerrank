# def func(a):
#     if(a%2==0):
#         return True
#     else:
#         return False
# print(func(int(input("Enter the number: "))))
# add=lambda a:print("Even") if a%2==0 else print("Odd")
# add(int(input()))
# add=lambda a:a%2==0
# add(int(input()))
# string=lambda str1:str1[len(str1)-1]
# print(string(input()))
# string=lambda str1:str1[::-1]
# print(string(input()))
# string=lambda str1,steps:str1[::steps+1]
# print(string(input("Enter string: "),int(input("Enter steps: "))))
string=lambda str1:print("True") if len(str1)>5 else print("False")
string(input("Enter the string: "))