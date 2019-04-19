i=1
size=int(input("Enter list size: "))
list=[]
while i<=size:
    x=int(input())
    list.append(x*x)
    i+=1
print(list)