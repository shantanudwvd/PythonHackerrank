winning_number=69
number=int(input("Guess a number: "))
if(number==winning_number):
    print("You Won")
else:
    if(number>=winning_number):
        print("Too High")
    else:
        print("Too low")