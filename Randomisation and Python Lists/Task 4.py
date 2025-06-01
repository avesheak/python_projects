##password Genarator 12 leanth

import random
import string

length = 12
random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
print(random_string)

## Coin Flip Game
import random
Coin = random.randint(0,1)
if Coin == 1:
    print ("Head")
else:
    print("Tail")

##Who will pay the bill 
list = ['Avesheak', 'Antim', 'Tushar', 'Ronok']
list.append("Taj")
print (list)

##Who will pay the bill 2.0
name = input("Give me names separated by commas (e.g., Alice, Bob, Charlie): ")
listname = name.split(", ")
names = len(listname)
random_index = random.randint(0, names - 1)
paythebill = listname[random_index]

print(f"{paythebill} is going to pay the bill!")

## rock paper scissors Game 

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_image = [rock, paper, scissors]
player = (int(input("0 for rock, 1 for paper, 2 for scissors")))
computer = random.randint(0,2)
print (f"You choice{player}")
print (game_image[player])
print (f"Computer choice{Computer}")
print (game_image[Computer])
#For Rock 
if player == 0 and computer == 0:
    print ("Draw")
elif player == 0  and computer == 1:
    print ("You win")
elif player == 0  and computer == 2:
    print ("You lose")

#For paper
if player == 1 and computer == 0:
    print ("You win")
elif player == 1  and computer == 1:
    print ("Draw")
elif player == 1  and computer == 2:
    print ("You lose")

##For scissors
if player == 2 and computer == 0:
    print ("You lose")
elif player == 2  and computer == 1:
    print ("Your win")
elif player == 2  and computer == 2:
    print ("Draw")