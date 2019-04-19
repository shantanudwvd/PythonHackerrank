mydict = {}
i = 0
mylist = []
val = []
size = int(input())
while i < size:
    mylist.append(input())
    idxs = idxe = j =0
    while j < 3:
        if j == 0:
            string = mylist[i]
            string = string + " "
        idxs = string.index(" ", idxs)
        idxs += 1
        idxe = string.index(" ", idxs)
        idxe -= 1
        val.append(float(string[idxs:idxe+1]))
        idxs = idxe
        j += 1
    average= sum(val)/3
    average=float(average)
    average=(format(average,'.2f'))
    k=0
    name=""
    while string[k]!=" ":
        name=name+string[k]
        k+=1
    mydict[name]=average
    val.clear()
    i += 1
query_name=input()
print(mydict.get(query_name))