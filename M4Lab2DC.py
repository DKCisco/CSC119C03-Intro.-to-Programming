# Drag to Draw Pygame program
# By C. Calongne 01/21/19
# Developed with tips from Pygame.com & Teach Your Kids to Code by Payne, 2015

# Six steps to complete in M4Lab2
# Define a list to store the colors
# Define statements for each mouse button
# Within the program suite, draw on screen with a different color
# When your program runs, a black box appears. 
# Draw with a different color using the left, middle, and right cursor buttons
# The middle cursor is the scrollwheel. You can configure a random color.
# Close the draw window. In the Python shell, type exit() to quit


import pygame
import random # optional for this program, but useful for random colors, such as
# randcolor = random.randrange(0,255)

pygame.init()

# Defines the display size with a width and height of 600, 600
size = width, height = 600, 600


# Step 1: Define a colors list to describe 3 colors.
# Hint, use their RGB number values
colors = [(255,0,0),(255,255,0),(0,255,0)]


screen = pygame.display.set_mode(size)
# Draws the screen using the size

pygame.display.set_caption("Click and drag to draw")
# Displays the title at the top of the draw screen

keep_going = True
# The program continues unti you close the window and type exit() in the shell

# Step 2: define a radius variable for your pen at 5, 10 or 15
# Test them to see which radius you prefer and use it.
radius = 5


mousedown = False
# we have not started drawing yet

while keep_going != False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going  = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousedown = True
        if event.type == pygame.MOUSEBUTTONUP:
            mousedown = False
            
    if mousedown: # start drawing
        spot = pygame.mouse.get_pos() # locate the pen's position as the 1st spot
        if pygame.mouse.get_pressed()[0]: # Boolean for button 1
            button_color = colors[0] # selects the first color from the list
            
        # Step 3: write the elif for pressing button 2, similar to button 1
        if pygame.mouse.get_pressed()[1]:

        
            # Step 4: write the statement for button 2's color
            button_color = colors[1]

        
        # Step 5: write the else statement for button 3
        if pygame.mouse.get_pressed()[2]:

        
            # Step 6: choose a color from the list
            button_color = colors[2]
     
           
        pygame.draw.circle(screen, button_color, spot, radius)
        # The pen is in the shape of a circle that draws on the screen
        # using the button color, the position of the spot, and the pen's radius

    pygame.display.update()
    # You can draw until you close the Pygame window

pygame.quit()

# Does the program continue to run?
# Type print(keep_going) or another variable to test it. 
# The program ends after you type exit() in the Python shell.

# For fun, try defining a random color and calling it for button_color
# randcolor = random.randrange(0,255)



