import pygame
import time
import random

health = 100
hunger = 0
disease = 0
time = 0
distance_remaining = 2000
food = 100
wheels = 4
oxen = 4
clothes = 5

print("Welcome to the Oregon Trail.")
name = ""
while name == "":
    name = input("What is your name?")
    for n in name.lower():
        if n not in "abcdefghijklmnopqrstuvwxyz":
            print("That's not valid, try again.")
            name = ""
            break
print(f"Hello {name.title()}.")
            