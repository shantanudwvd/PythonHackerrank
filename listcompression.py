# def listcompression(mylist):
#     return[i for i in mylist if(type(i)==int or type(i)==float)]
# print(listcompression([True,False,'abc',1,2,3,3,22.0]))
def listcompression(age):
    return[print("not allowed") if(age<=3) else print("Allowed")]
# number=list(range(1,11))
# print(number)
# print(listcompression(number))
age=int(input("Enter your age: "))
listcompression(age)