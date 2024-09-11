# Task 2: Setting the Scene. Based on your corrected code from Task 1, 
# expand the game. If the user chooses "cave", 
# ask them if they want to "light a torch" or "proceed in the dark", 
# and provide outcomes for each decision.

place = input("Choose a place: forest or cave? ")

if place == "forest": #Use of == vs =
    action = input("climb a tree or cross a river?")
    if action == "climb a tree": #Use of == vs =
        print("You found a bird's nest!")
    elif action == "cross a river": #Use of == vs = & elif vs else
        print("You found a boat!")
elif place == "cave": #Use of == vs =
    light = input("Do you want to light a torch? Yes/No ")
    if light == "Yes":
        print("You find a hidden treasure!")
    else:
        print("You trip, break a leg, and are never found...")

    