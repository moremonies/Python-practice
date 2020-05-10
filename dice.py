import random

def dice_roll():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    return dice1 + dice2

input("Press enter to play the dice game: ")


player = dice_roll()
computer = dice_roll()

if player > computer:
    print("You win! Your number was " + str(player) + ". The computers number was " + str(computer) + ".")
if player < computer:
    print("The computer won! Your number was " + str(player) + ". The computer had " + str(computer) + "!")
if player == computer:
    print("There was a tie! You both had " + str(player))






#dice1 = random.randint(1,6)
#dice2 = random.randint(1,6)
#print(str(dice1) + " " + str(dice2))