n=int(input())
mylist=list(map(int,input().split()))
t=tuple(mylist)
print(hash(t))

