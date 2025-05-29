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
name = input("Give me Names with , for who will pay the bill")
listname = name.split(", ")
pay = listname[random_choice]