print ("Hello" [3])

#Data Type 
num_char = input("What is your name")
print (type(num_char))

#Data type example two
num_char = (len(input("What is your name")))
print (type(num_char))

#Type Casting 
char = len((input("What is your Name")))
new_char = str(char)
print ("Your name has " + new_char + " Character")

#challenge

a = input("Put First Number")
b = input ("Put Secound number")
new_a = int(a)
new_b = int(b)
print (new_a+new_b)

#challenge
put_two_digit_number = input("Put Two Digit Number")
first_number = put_two_digit_number[0]
secound_number = put_two_digit_number[1]
print(int(first_number) + int(secound_number))

#BMI Calculator
e = input("Put your body weight in KG")
f = input("Put your height in m")
g = float(e) / (float(f) * float(f))
print (int(g))

#Tip Calculator
print ("Welcome to our Tip Calculator")
bill = (int(input("What IS your Bill Amount")))
Tipammount = (int(input("What is the amount percentage you want to give 10, 12, 20")))
totaltipamount = (bill * (Tipammount/100))
totalbill = (bill+totaltipamount)
print (round(totalbill),2)