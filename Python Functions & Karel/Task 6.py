def myfunction():
    print ("Hello World")
myfunction()

## This code is only run on https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
## It will not work here.
def movement():
    move()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
for com in range(6):
    movement()

##Finding goal with while loop & Function 
def movement():
    move()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
while at_goal() == False:
    movement()

## Stage 3 Issue 
while at_goal() == False:
    if front_is_clear() == True:
        move()
    elif wall_in_front() == True:
        turn_left()
        move()
        turn_left()
        turn_left()
        turn_left()
        move()
        turn_left()
        turn_left()
        turn_left()
        move()
        turn_left()
        