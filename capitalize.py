def solve(s):
    string=""
    s=s+" "
    i=j=0
    while i<=len(s)-1:
        str=""
        while s[j]!=" ":
            if len(s)==j:
                break
            str=str+s[j]
            j+=1
        k=0
        while k<len(str):
            if k==0:
                string=string+str[0].upper()
            else:
                string=string+str[k]
            k+=1
        string=string+" "
        j+=1
        i=j
    return string

s = input()
result = solve(s)
print(result)
