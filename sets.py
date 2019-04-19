# square={k**2 for k in range(1,11)}
# print(square)
# name={"rohit","mohit","shantanu","ram","seeta"}
# print(name)
# def alltotal(*args):
#     total=0
#     for num in args:
#         total+=num
#     return total
# print(alltotal(1,2,3,4))
# def alltotal(*args):
#     args=list(args)
#     nums=0
#     while nums<len(args):
#         args[nums]=args[nums]/2
#         nums+=1
#     args=tuple(args)
#     return args
# print(alltotal(1,2,3,4))
# def alltotal(*args):
#     for num in range(0,len(args)):
#         args=list(args)
#         div=args[num]/2
#         args[num]=div
#     return args
# print(alltotal(5,7,8,6))
# def alltotal(num1,*args):
#     total=0
#     print(num1)
#     for num in args:
#         total+=num
#     return total
# print(alltotal(4,5))
# ARGS AS ARGUEMENT
# def alltotal(*args):
#     multiply=1
#     print(args)
#     for num in args:
#         multiply*=num
#     return multiply
# nums=[1,2,3]
# print(alltotal(*nums))
#ASSIGNEMENT
# def alltotal(n,*args):
#     args=list(args)
#     i=0
#     while i<len(args):
#         args[i]=pow(args[i],n)
#         i+=1
#     print(args)
# size=int(input("Enter the input: "))
# nums=[1,2,3,4,5]
# if(size==0):
#     print("Hey, you are fucked")
# else:
#     print(alltotal(size,*nums))
def alltotal(size,*args):
    args=list(args)
    return[pow(i,size) for i in args]
size=int(input("Enter the input: "))
nums=[1,2,3,4,5]
if(size==0):
    print("Hey, you didnt give a valid input")
else:
    print(alltotal(size,*nums))
