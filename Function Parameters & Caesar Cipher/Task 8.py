def name(name, location):
    print(f"What is your {name}")
    print(f"What is your {location}")

name("Avesheak", "Bangladesh")

## python keywords arguments
def name(name, location, massage="nice"):
    print(f"What is your {name}")
    print(f"What is your {location} it is a nice {massage} country")

name("Avesheak", "Bangladesh")

#8.1 Challenge 
def total (height, width, cover):
    area=height*width
    num_of_cans=round(area/cover)
    print(f"You will need {num_of_cans} cans to cover the {cover}")
height = (float(input("Put Total height: ")))
width = (float(input("Put Total width: ")))
cover = (float(input("Put Total area: ")))
total(height,width,cover)

## Prime Number Checking 
def prime_number():
    for a in range(2, 100):  
        is_prime = True
        for i in range(2, int(a ** 0.5) + 1): 
            if a % i == 0:
                is_prime = False
                break
        if is_prime:
            print(a)

prime_number()

## Prime Number checking 2.0 
def pnum(number):
    pnum_Stat = True
    for i in range(2,number):
        if number % i == 0:
            pnum_Stat = False
    if pnum_Stat:
        print("It is prime number")
    else:
        print("Not a prime number")
number = int(input("Put a number here"))
pnum(number)

## Chiper Text

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
def encrypt(text,shift):
    chiper_text = ""
    for letter in text:
        possiction = alphabet.index(letter)
        new_possition = possiction + shift
        decript = alphabet[new_possition]
        chiper_text += decript
    print (f"Your encoded text is {chiper_text}")

def deencrypt (text,shift):
    chiper_text = ""
    for letter in text:
        possiction = alphabet.index(letter)
        new_possition = possiction - shift
        decript = alphabet[new_possition]
        chiper_text += decript
    print (f"Your decode text is {chiper_text}")
if direction == "encode":
    encrypt(text,shift)
elif direction == "decode":
    deencrypt(text,shift)
else:
    print("You put a wrong input")

## Optimizing the cipher code
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def small (direction,text,shift):
    cipher_text= ""
    if direction == "encode":
        encrypt(text,shift)
    elif direction == "decode":
        deencrypt(text,shift)
    else:
        print("You put a wrong input")
from art import logo







