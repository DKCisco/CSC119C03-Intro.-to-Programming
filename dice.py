# Lab assignment inspired by E. Matthes
# Randomly rolls a 6-sided die

from random import randint
class Dice():
    """A class for a single six-sided die"""

    def __init__(self, dice_sides=6):
        """A six-sided die."""
        self.dice_sides = dice_sides

    def roll(self):
        """Returns a random value between 1 and the number of sides."""
        return randint(1, self.dice_sides)
