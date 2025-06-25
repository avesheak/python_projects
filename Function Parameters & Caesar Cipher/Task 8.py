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
