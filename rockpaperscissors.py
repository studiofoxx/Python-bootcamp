import random
#import mymodule

#import GameLoad.py
#this is supposed to be ran at the start, decided to make it a seperate script
#called GameLoad.py. now to figure out how add scripts as modules
#print("Would you like to play a game?\nY/N?")

##prints a random number between 1 and 10
rock = 1
paper = 2
scissors = 3

random_integer = random.randint(1, 3)
print(random_integer)

##prints a random number between 0 and 4
##then adds 1 to get 1 to 5
#random_float = random.random()
#random_float * 5
#print (int(random_float * 5 + 1))


##imports mymodule.py and prints verbose
##not using, just there for refrence
#print(mymodule.pi)