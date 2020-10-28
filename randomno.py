import random
number = random.randint(1,3)
guess = int(input("guess a number between 1 to 3:"))

if guess > number:
    print("guess no is higher than random")
    guess = int(input("guess a number between 1 to 3:"))
elif guess < number:
    print("guess no is lower than random")
    guess = int(input("guess a number between 1 to 3:"))
else:
    print("you got the correct no")
