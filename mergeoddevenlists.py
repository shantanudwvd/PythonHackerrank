list=[]
print("Enter the size: ")
size=int(input())
i=1
while i<=size:
    list.append(input())
    i+=1
print(list)
even=[]
odd=[]
j=0
while j<size:
    idx=int(list[j])
    if(idx%2==0):
        even.append(list[j])
    else:
        odd.append(list[j])
    j+=1
print(even)
print(odd)