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
player = 0
dealer = 0

def player():
    print(x1,x2)
    sum1= x1 + y1
    return sum1

def banker():
    print(x2+y2)
    sum2= x2 + y2
    return sum2

def morecards():
    print(z1)
    if show_more_card =="y":
        print("New Card", z1)
        sum = x1+y1+z1
        return sum


player_total=player()
banker_total=banker()
print("Lets start the game")
print(f"Starting by the player {player_total}")


