#Task 3: Catering Choices. Ask the user if they want "vegetarian" food. 
# Recommend "Veggie Delight Caterers" if yes, otherwise 
# recommend "Gourmet Meals Caterers".

attendees = int(input("Enter number of attendees: "))
vegetarian = input("Is a vegetarian menu needed? Yes/No ")
venue = "Large hall" if attendees > 50 else "conference room"
print(venue)
podium = "Stage w/ poduim" if attendees > 50 else "Just a podium"
print(podium)
refreshments = "Fruit, chips, candies, sodas, and waters" if attendees > 50 else "Chips and water"
print(refreshments)
name_tags = "Laid at each seat with a complimentary pen" if attendees > 50 else "Distributed at check in"
print(name_tags)
catering = "Veggie Delight Caterers" if vegetarian == "Yes" else "Gourment Meal Caterers"
print(catering)