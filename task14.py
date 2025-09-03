from random import randint

def roll_dice():
    return randint(1, 6), randint(1, 6)

def show_dice(dice):
    dice_sides = {}