import sys
m=int(input())
list1=set(map(int,input().split()))
n=int(input())
ans=[]
list2=set(map(int,input().split()))
ans=list(list1.difference(list2))
ans1=list(list2.difference(list1))
fin=ans+ans1
fin.sort()
for i in range(0,len(fin)):
    print(fin[i])