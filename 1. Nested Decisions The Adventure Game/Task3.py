# Task 3: Default Path. If the user makes an invalid choice at any point, 
# incorporate a pass statement to handle it. 
# HINT: How can an else statement be of use here?

place = input("Choose a place: forest or cave? ")

if place == "forest": #Use of == vs =
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree": #Use of == vs =
        print("You found a bird's nest!")
    elif action == "cross a river": #Use of == vs = & elif vs else
        print("You found a boat!")
    else:
        pass
elif place == "cave": #Use of == vs =
    light = input("Do you want to light a torch? Yes/No ")
    if light == "Yes":
        print("You find a hidden treasure!")
    elif light != "Yes":
        print("You trip, break a leg, and are never found...")
    else:
        pass
else:
    pass

#This seems like to simple a solution...