# Guessing game
import random
guesses_taken = 0

# Get name and explain game
name = input("Hello and welcome to Dans guessing game! Whats your name? " )
print("Hello " + name.capitalize() + "! I'm thinking of a number from 1 to 20. You will get 6 try's to guess the number im thinking!" )

# Get random number that player guesses
number = random.randint(1, 20)

# loop for the 6 guesses

for guesses_taken in range(6):
    guess = input("Ok take your guess: ")
    guess = int(guess)

    if guess < number:
        print("Your guess was to low. Try again!")

    if guess > number:
        print("Your guess was to high. Try again!")

    if guess == number:
        break
# Loop breaks if its = and prints the outcome
if guess == number:
    guesses_taken = str(guesses_taken + 1)
    print("Good job " + name.capitalize() + "! It took you " + guesses_taken + " try's to guess the number!")

# Loop breaks after 6 attempts and prints they lost and what the number is

if guess != number:
    number = str(number)
    print("The number I was thinking was " + str(number) + "!")






