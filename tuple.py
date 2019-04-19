def fun(a,b):
    add=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return add,sub,mul,div
add,sub,mul,div=fun(int(input()),int(input()))
print(add)
print(sub)
print(mul)
print(div)