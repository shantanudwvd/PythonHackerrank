def func(int1,int2):
    add=int1+int2
    mul=int1*int2
    return add,mul
add1,mul1=func(int(input("Enter first number: ")),int(input("Emter second number: ")))
print("sum is:",add1)
print("multiplication is:",mul1)