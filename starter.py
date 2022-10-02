import random

random_number = random.randint(1,10)  # numbers 1 - 10
print(random_number)
# handle user guesses
#   if they guess correct, tell them they won
#     otherwise tell them if they are too high or too low

# BONUS - let player play again if they want!

guess = None

while guess != random_number:
    guess = input("Enter a number from 1 - 10: ")
    guess = int(guess)  
    if guess == random_number:
        print("YOU GOT IT!")
    elif guess < random_number:
        print("TOO LOW!")
    else:
        print("TOO HIGH!")