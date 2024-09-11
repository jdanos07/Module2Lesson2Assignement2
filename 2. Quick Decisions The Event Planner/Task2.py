# Task 2: Venue Selection. Based on the corrected code from Task 1, 
# further enhance your code to recommend additional things 
# like "audio system" or "projector" based on the number of attendees.

attendees = int(input("Enter number of attendees: "))
venue = "Large hall" if attendees > 50 else "conference room"
print(venue)
podium = "Stage w/ poduim" if attendees > 50 else "Just a podium"
print(podium)
refreshments = "Fruit, chips, candies, sodas, and waters" if attendees > 50 else "Chips and water"
print(refreshments)
name_tags = "Laid at each seat with a complimentary pen" if attendees > 50 else "Distributed at check in"
print(name_tags)