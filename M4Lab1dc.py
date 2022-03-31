# Calculator Program
# M4Lab1dc.py for M4 Assignment 1
# Dillan Craig 3/30/2022

# Seven steps to complete in this lab: 
# Define a list to store the choices for +, -, *, /
# Define 3 functions with local variables
# Define three elif statements that call the functions for -, *, and /

# Local variables are visible in the functions
# Pass the input values into them.
# Continue calculating until the user presses "n"

print("Welcome to your Calculator program")

# The add function adds two numbers 
def add(x, y):
   return x + y
   # local scope; only the add() function sees x and y

#write the other three functions for subtract, multiply and divide

# Step 1: Write a subtract function that subtracts two numbers 
def sub(x, y):
    return x - y

# Step 2: Write a multiply function that multiplies two numbers
def mul(x, y):
    return x * y

# Step 3: Write a divide function that divides two numbers
def div(x, y):
    return x / y

# Start calculating 
# Step 4: define a list called choice with + - * / in it
math=['+','-','*','/']

keep_going = ["y", "n"] # only tests for "n"

while keep_going != "n":

    num1 = float(input("Enter first number: "))
    choice = input("What kind of calculation? Choose one of: +, -, *, /  ")
    num2 = float(input("Enter second number: "))

    if choice == "+":
        # choice is a list with the string value for "+"
        # The test for choice returns the value True or False. If true:

        print(num1, choice, num2,"=", add(num1,num2))
        # calls the add function and passing it two parameters

    # finish the rest of the if statement for the other 3 calculations
                           
    # Step 5: write an elif for subtract
    elif choice == math[1]:
        print(num1, choice, num2,"=", sub(num1,num2))

    # Step 6: write an elif for multiply
    elif choice == math[2]:
        print(num1, choice, num2, "=", mul(num1,num2))

    # Step 7: write an elif for divide
    elif choice == math[3]:
        print(num1, choice, num2,"=", div(num1,num2))
    
    else:
        print("Invalid input")

    keep_going = input("Calculate? y or n? ")    
print("Closing the calculator.")
