Student_score = {
    "Rakib": 85,
    "Rifat": 89,
    "Avesheak": 95,
    "Taj": 25,
    "Antim": 86,
}
print(Student_score["Avesheak"])
print (Student_score["Taj"])
for grade in Student_score:
    if (Student_score[grade]) >= 91:
        print("OutStanding")
    elif (Student_score[grade]) >= 81:
        print("Grate")
    if (Student_score[grade]) >= 71:
        print("Good")
    else:
        print("Fail")

## Travel Log: 
Bangladesh = {
    "Dhaka" : {"City I visited" : ["Mirpur" , "Tejgaon", "Dhanmondi"], "total visit": 12},
     "East_india" :{"City I visited":["Gujrat", "Rajasthan", "Mumbai"], "City total visit": 12}
}
## 9.2 Test
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
def add_new_country(country_visited,time_visited, city_visited ):
    new_country={}
    new_country["country"]=country_visited
    new_country["visits"]=time_visited
    new_country["cities"]=city_visited
    travel_log.append(new_country)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

# Bidding game 
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
total_user={}
status = input("Is here anyone available for bid? Yes/No").lower()
while status == "yes":
    if status == "yes":
        user = input("What is your name")
        bid = int(input("Put the bid amount $"))
        total_user[user]=bid
        status = input("Is here anyone available for bid? yes/no").lower()
    elif status == "no":
        print("No user to bid")
    else:
        print("You put a wrong inpute")
def height_bid():
    height = max(total_user, key=total_user.get)
    highest_amount = total_user[height]
    print(f"The highest bidder is {height} with a bid of ${highest_amount}.")

height_bid()
