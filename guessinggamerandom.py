import random
winning_number=random.randint(1,100)
count=0
while(True):
    guess = int(input("Enter Your Guess: "))
    if(guess==winning_number):
        print("You Won and your total guesses are",count)
        break;
    elif(guess>winning_number):
        print("Too High")
        count+=1
    elif(guess<winning_number):
        print("Too Low")
        count+=1
