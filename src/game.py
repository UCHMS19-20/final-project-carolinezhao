import pygame
import time
import random

health = 100
hunger = 0
disease = 0
days = 0
distance_remaining = 2000
food = 100
wheels = 4
oxen = 4
clothes = 5

print("Welcome to the Oregon Trail.")
time.sleep(1)
name = ""
while name == "":
    name = input("What is your name? ")
    for n in name.lower():
        if n not in "abcdefghijklmnopqrstuvwxyz":
            print("That's not valid, try again.")
            name = ""
            break
print(f"Hello {name.title()}.")
time.sleep(1)
print("Right now, we are in Independence, Missouri.")
time.sleep(1)
print("You want to go out west, and the Oregon Trail is the best way to do so.")
time.sleep(1)
print("Today is April 1st. Your goal is to make it to Oregon before December 15, when winter will fall.")
time.sleep(1)
print("It's a dangerous journey, but I have faith in you. Good luck!")