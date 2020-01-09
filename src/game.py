import pygame
import time
import random

health = 100
typhoid = False
cholera = False
dysentery = False
days = 0
distance = 2000
food = 500
wheels = 4
oxen = 4
clothes = 5
diseases = []

def status():
  print("Your current status is as follows:")
  if health >= 75:
    print("Health: Good")
  elif 75 > health >= 50:
    print("Health: Fair")
  else:
    print("Health: Poor")
  if diseases == []:
    print("Disease(s) Present: None")
  else:
    print(f"Disease(s) Present: {', '.join(diseases)}")
  print(f"Food Supply: {food} lbs")
  print(f"Clothing: {clothes} sets")
  print(f"Oxen: {oxen}")
  print(f"Wagon Wheel(s): {wheels}")
  print(f"Days since April 1st: {days}")
  print(f"Days until December 15th: {258-days}")
  print(f"Distance Remaining: {distance} miles")
  return


status()
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
time.sleep(1.5)
print("You want to go out west, and the Oregon Trail is the best way to do so.")
time.sleep(1.5)
print("Today is April 1st. Your goal is to make it to Oregon before December 15, when winter will fall.")
time.sleep(1.5)
print("It's a dangerous journey, but I have faith in you. Good luck!")
