mylist=[]
queries=int(input())
i=0
mylist1=[]
while i<queries:
    mylist1.append(input())
    if "insert" in mylist1[i]:
        string=mylist1[i]
        idxs=mylist1[i].index(" ")
        idxs=idxs+1
        idxe=mylist1[i].index(" ",idxs)
        idxe-=1
        vals=mylist1[i].index(" ",idxe)
        vals+=1
        index=string[idxs:idxe+1]
        index=int(index)
        value=string[vals:]
        value=int(value)
        mylist.insert(index,value)
    elif "print" in mylist1[i]:
        print(mylist)
    elif "remove" in mylist1[i]:
        string=mylist1[i]
        idx=mylist1[i].index(" ")
        idx+=1
        value=string[idx:]
        value=int(value)
        mylist.remove(value)
    elif "append" in mylist1[i]:
        string=mylist1[i]
        idx=mylist1[i].index(" ")
        idx+=1
        value=string[idx:]
        value=int(value)
        mylist.append(value)
    elif "sort" in mylist1[i]:
        mylist.sort()
    elif "pop" in mylist1[i]:
        mylist.pop()
    elif "reverse" in mylist1[i]:
        mylist.reverse();
    i+=1