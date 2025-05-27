choice = (input("Where you want to go left or right")).lower()
print (choice)

# Digital booking system 
bill = 0
print("Welcome to our Ticket Booking System")
height = int(input("Put your height in CM: "))

if height >= 192:
    print("You are ok for riding")
    age = int(input("Put your age: "))
    if age >= 18:
        print("Your price is $12")
        bill = 12
    else:
        print("Your ticket price is $7")
        bill = 7

    photo = input("Do you want a photo? (yes or no): ").lower()
    if photo == "yes":
        bill += 5

    print(f"Your total amount is ${bill}")
else:
    print("You are not able to ride")



## BMI 2.0 

theight = (int(input("Put your Height")))
tweight = (int(input("Put your weight")))
bmi = round(tweight/theight**2)
if bmi < 18.5:
    print (f"Your bmi is {bmi} underweighted")
elif bmi < 25:
    print (f"Your bmi is {bmi} Normal Weight")
elif bmi < 30:
    print (f"Your bmi is {bmi} overweighted")
elif bmi < 35:
    print (f"Your bmi is {bmi} obese")
else:
    print (f"Your bmi is {bmi} extra weight")


#Pizza Order system 
bill1 = 0

choice1 = (input("Which pizza Size you want Small, Medium or Large")) .lower()
if choice1 == "small":
    bill1 = 15
    peppsmall = (input("Do you want pepperoni for extra 2$ Yes or Not").lower())
    if peppsmall == "yes":
        bill1 += 2
elif choice1 == "medium":
    bill1 = 20
    peppsmall = (input("Do you want pepperoni for extra 3$ Yes or Not").lower())
    if peppsmall == "yes":
        bill1 += 3
elif choice1 == "large":
    bill1 = 25
    peppsmall = (input("Do you want pepperoni for extra 3$ Yes or Not").lower())
    if peppsmall == "yes":
        bill1 += 3
cheese = (input("Do you want cheese  for extra 1$ Yes or Not").lower())
if peppsmall == "yes":
    bill1 += 1
else:
    print ("You have wrong inpute")
print (f"Your Total Ammount is {bill1}")