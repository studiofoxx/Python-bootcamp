import random
#import mymodule
#import GameLoad.py
#this is supposed to be ran at the start, decided to make it a seperate script
#called GameLoad.py. now to figure out how add scripts as modules
#print("Would you like to play a game?\nY/N?")

##prints a random number between 1 and 3
#rock = 1
#paper = 2
#scissors = 3

#this is right
moves = ["rock", "paper", "scissors"]
#ask the user for input of rock, paper, or scissors

print ("time to play")

#testcode to see if variables are working. outouts 1 2
#print(moves)
#insert timewait here for a few seconds to space out words
print("rock = 0 paper = 1 scissors = 2 \nwhat number do you choose?")
userchoice = int(input())
print ("you picked ", (moves[userchoice]))

#pc logis is sound. picks a random number and 
random_integer = random.randint (1, 3)-1
#random_integer = random.randint(1, 3)
print ("computer picks: ", (moves[random_integer]))



#problem solving lines below
if userchoice == random_integer:
    print("you tie")
elif userchoice == 0 and random_integer == 2:
    print("you win")
elif random_integer == 0 and userchoice == 2:
    print("you lose")
elif random_integer == 1 and userchoice == 0:
    print("you lose")
elif random_integer == 1 and userchoice == 2:
    print("you win")
elif userchoice == 1 and random_integer == 2:
    print("you lose")
elif userchoice == 1 and random_integer == 0:
    print("you win")
elif userchoice < 2:
    print("not good at following between the lines, huh?")
#print("computer picks", random_integer)

#to make things easier make a list and call from list
#only thing that should be on the list is rock, paper, scissors
#convert that to a string
