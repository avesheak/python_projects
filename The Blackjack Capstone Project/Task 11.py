#version 1

import random

#player card

x1 = random.randint (1, 10)
y1= random.randint (1, 10)
z1= random.randint (1, 10)

#bancker card

x2 = random.randint (1, 10)
y2= random.randint (1, 10)
z2= random.randint (1, 10)

def player():
    sum1= x1 + y1
    return sum1

def banker():
    sum2= x2 + y2
    return sum2

def morecards(choice):
    if choice =="y":
        print("New Card", z1)
        sum = x1+y1+z1
        if player() < banker():
            print("Player Win")
    elif player() > banker():
        print("Banker win")
    else: print("Draw")
    

def function():
    print("Lets start the game")
    print(f"The player score is {player()}")
    choice=input(print("DO you want to draw more card Press y")).lower()
    morecards(choice)
    test
    
function()