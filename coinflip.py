import random
flips = 0
heads = 0
tails = 0

print("This program will display the results of a coin being flipped 1000 times! ")
while flips < 1000:
    if random.randint(0,1) == 0:
        heads += 1
        flips += 1
    if random.randint(0,1) == 1:
        tails += 1
        flips += 1
    if flips == 500:
        print("At 500 flips there were " + str(heads) + "  heads and " + str(tails) + " tails.")
print("Tails " + str(tails))
print("Heads" + str(heads))
