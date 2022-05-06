# Module 5 Lab 2 asks you to work with two Python files
# Lab inspired by E. Matthes, adapted on 4/8/19 by C. Calongne
# This program calls the Dice class and rolls a six-sided dice 1000 times
# Both the dice.py and the M5Lab2dice_hist.py files must be in the same folder
# You can rename your lab.py file, but do not change dice.py

# pygal draws a bar chart (a histogram) and saves it as a .svg file
# Install pygal from the Module 3 Exploration before completing this lab.
# Complete Steps 1-8 listed in the code.
#
# What Lab 5 does:
# ************************
# It randomly rolls a 6-sided die a # of times based on the range(value)
# If range(100), then it rolls a single die 100 times
# Stores the values in a results[] list
# Uses pygal to create a bar chart with
# A title across the top
# An x axis title at the bottom of the chart along the x axis
# A y title going up the left side's y axis
# Creates a dice_barchart.svg chart in the folder with this program.
# Drag the dice_barchart.svg file and drop it on a browser window to see the chart
# Hover over the bar chart to see the total numbers rolled for 1-6
# See the M5 Exploration and the two examples files: dog.py and dog_new.py

# Your program begins here - do not forget to update the pseudocode and post it.
# ************************

import pygal
# Similar to the Dog example in the Module 5 Exploration and the two dog files

# Step 1: import from dice the Dice class
from dice import Dice


# Step 2: For the variable name dice, assign the Dice() class
dice = Dice()

# Step 3: Declare an empty results list
results = []
     #results=[]

# Step 4: Roll the dice 1000 times 

for roll_num in range(1000):
# stores the results for each single dice roll in a list
    result = dice.roll()
    results.append(result)

# analyze the results
frequencies = []

# range starts at 0, increments by 1 and stops just before the last number
# Uses +1 to stop just before 7 for 1-6 sides

for value in range(1, dice.dice_sides +1):
    
# Step 5: call the value as you count the results
    frequency = results.count(value)
# Step 6: similar to the results list, keep appending or adding the frequency
    frequencies.append(frequency)

# Step 7: Print the frequencies to the Python Shell
print(frequencies)

# creates a bar chart to display the results
hist = pygal.Bar()

# Step 8: use your name in the bar chart's title

hist.title = "Dillan Craig's Results from 1000 Dice Rolls"
# This section describes the labels for the bars in a bar chart
# You can change these labels, but for your first run, see how the chart looks first.

hist.x_labels = ["1", "2", "3", "4", "5", "6"]
hist.x_title = "Result" # displays at the bottom of the chart
hist.y_title = "How Often Did We Roll a 1, 2, 3, 4, 5, or 6?"

hist.add("D6", frequencies)
hist.render_to_file("dice_barchart.svg")

# Drag your dice_barchart.svg file in your .py folder to an empty browser window
# See your chart appear, hover over it with your cursor, and examine the labels
# Congratulations! 
