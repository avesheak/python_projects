#For loop condiction
total_number = 0
for total_number in range(10):
    print(total_number)
# Student Avarage Height
height = input("Put your student height separated by comma: ").split(",")
for n in range(len(height)):
    height[n] = int(height[n])
leanth = (len(height))
total_height = (sum(height))
avarage = total_height / leanth
print (avarage)

#Student height in for loop 2.0 
height = input("Put your student height separated by comma: ").split(", ")
total_height = 0
for h in height:
    total_height += int(h)
print (total_height)

total_number = 0
for number in height:
    total_number += int(number)
total_number = len(height)
print (total_number)
avarage = total_height/total_number
print (avarage)


## Max Number finding
scores = input("Put your student numbers").split(", ")
height_score = 0
for total_score in scores:
    if int(total_score) > height_score:
        height_score = int(total_score)
print (height_score)

##minumum Number finding 

student_scores = input("Put all student scores separated by , ").split(', ')
lowest_score = int(student_scores[0])  # Start with the first score

for score1 in student_scores:
    if int(score1) > lowest_score:
        lowest_score = int(score1)

print("Lowest score is:", lowest_score)



##Max number finding 2.0 
student_scores = input("Put all student scores separated by , ").split(', ')
height_score1 = int(student_scores[0])  # Start with the first score

for score2 in student_scores:
    if int(score2) > height_score1:
        height_score1 = int(score2)

print (height_score1)

## Adding total even number in loop
number_add=0
for num in range(2,101,2):
    number_add += num
print (number_add)

##fizbuzz game

for game in range(1,101):
    if game % 3 == 0 and game % 5 == 0:
        print ("Fizzbuzz")
    elif game % 3 == 0:
        print ("Fizz")
    elif game % 5 == 0:
        print ("Bazz")
    else:
        print (game)

#Random Password Genarator: 
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
nr_alphabate = int(input("Put how many alphabate your want"))
nr_numbers = int(input("Put how many numbers your want"))
nr_simbol= int(input("Put how many simbol your want"))
password = []

for pa in range(nr_alphabate):
    password.append(random.choice(letters))
for pa in range(nr_numbers):
    password.append(random.choice(numbers))
for pa in range(nr_simbol):
    password.append(random.choice(symbols))
print (password)
random.shuffle(password)
join = ''.join(password)
print (join)

