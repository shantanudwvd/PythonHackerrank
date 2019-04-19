# nested=[[i for i in range(1,4)] for j in range(3)]
# print(nested)
# square=[i**2 for i in range(1,11)]
# print(square)
# oddeven={i:("even" if i%2==0 else "odd")  for i in range(1,11)}
# print(oddeven)
# square={f"square of {num} is: ":num**2 for num in range(1,11)}
# for k,v in square.items():
#     print(f"{k}:{v}")
# print(square)
string=input("Enter a string: ")
wordcount={char:string.count(char) for char in string}
for k,v in wordcount.items():
    print(f"{k}:{v}")
# print(wordcount)