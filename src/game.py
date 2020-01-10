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
money = 500
diseases = []

def intro():
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
  return

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
  print(f"Money: ${money}")
  print(f"Food Supply: {food} lbs")
  print(f"Clothing: {clothes} sets")
  print(f"Oxen: {oxen}")
  print(f"Wagon Wheel(s): {wheels}")
  print(f"Days since April 1st: {days}")
  print(f"Days until December 15th: {258-days}")
  print(f"Distance Remaining: {distance} miles")
  return

def choose_an_option(days):
  print("\n")
  time.sleep(1)
  print(f"This is day {1+days} of your trip.")
  time.sleep(1)
  status()
  print("\n")
  time.sleep(1)
  print("Today, you may")
  print("1. Travel towards your destination")
  print("2. Rest and regain a bit of health")
  print("3. Engage in a random purchase")
  print("4. Hunt for a random amount of food")
  print("When picking your option, please only input the number of the activity you would like to do.")
  
  option = ""
  while option == "":
    option = input("What would you like to do today? ")
    if option not in "1234":
      option = ""
      time.sleep(1)
      print("That's not valid. Try again. The option must be an integer, either 1, 2, 3, or 4, depending on what you would like to do today.")
    elif len(option) > 1:
      option = ""
      time.sleep(1)
      print("That's not valid. Try again. The option must be an integer, either 1, 2, 3, or 4, depending on what you would like to do today.")
    elif len(option) < 1:
      option = ""
      time.sleep(1)
      print("That's not valid. Try again. The option must be an integer, either 1, 2, 3, or 4, depending on what you would like to do today.")
    else:
      return option 

def travel(health):
  if health >= 75:
    distance_travelled = random.randint(12, 18)
  elif 75 > health >= 50:
    distance_travelled = random.randint(7, 13)
  else:
    distance_travelled = random.randint(5, 7)  
  print(f"You travelled {distance_travelled} miles.")
  return(distance_travelled)

def rest():
  return 

def buy():
  return

def hunt():
  possible_food_gains = [0, 20, 40, 60, 80, 100]
  index = random.randint(0,5)
  food_gain = possible_food_gains[index]
  print(f"You gained {food_gain} lbs of food.")
  return(food_gain)
