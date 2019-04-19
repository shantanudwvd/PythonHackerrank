size=int(input())
i=0
name=[]
number=[]
list=[]
while i<size:
    name.append(input())
    number.append(float(input()))
    list.append(number[i])
    i+=1
list.sort()
i=1;
min=list[0]
while i<len(list):
    if(list[i]!=min):
        min=list[i]
        break
    i+=1
i=0
ans=[]
while i<len(number):
    if(min==number[i]):
        ans.append(name[i])
    i+=1
ans.sort()
i=0
while i<len(name):
    print(ans[i])
    i+=1