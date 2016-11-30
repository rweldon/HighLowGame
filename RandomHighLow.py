import random

number = random.randrange(0,50)

guess = -1


print("Guess the number!")
while guess != number:
    guess = int(input("Is it.."))

    if guess == number:
        print("Hooray you got it!")

    elif guess < number:
        print("Too low, try higher..")

    elif guess > number:
        print("Too high, try lower")
