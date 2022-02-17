# M2Lab2 Written by Dillan Craig 2/17/2022

print("Welcome, you have won a free vacation with airfare and hotel expenses paid!")

# Get users name from input and assign to variable
users_name = input("What is your name? ")

# Determine where user wants to go on vacation from input and assign to variable
vacation_location = input("Where do you want to go on vacation? ")

# Display the location of vacation
print("Your desired vacation location is",vacation_location, "!")

# Determine how many days user wants to go on vacation from input and assign to variable
vacation_days = int(input("How many days will you spend on vacation, 4 or 7? "))

# Create a variable and calculate the cost of the vacation by multiplying vacation_days variable by 100
vacation_cost = vacation_days * 100

# Display variable that calculates the cost
print("The total cost for food and entertainment will be $", vacation_cost)

