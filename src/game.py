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
game = True

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
      print("\n")
      return option 

def travel():
  what_to_judge_travel_by = random.randint(1,3)
  if what_to_judge_travel_by == 1:
      if health >= 75:
        distance_travelled = random.randint(12, 18)
      elif 75 > health >= 50:
        distance_travelled = random.randint(7, 13)
      else:
            distance_travelled = random.randint(5, 7)
  if what_to_judge_travel_by == 2:
      if oxen > 4:
        distance_travelled = random.randint(14, 20)
      elif 4 >= oxen > 2:
        distance_travelled = random.randint(7, 14)
      elif oxen =< 0:
        distance_travelled = 1
      else:
            distance_travelled = random.randint(5, 7)
  if what_to_judge_travel_by == 3:
      if wheels >=4:
        distance_travelled = random.randint(12, 18)
      elif wheels =< 0:
        distance_travelled = 1
      else:
            distance_travelled = random.randint(5, 11)
  print(f"You travelled {distance_travelled} miles.")
  return(distance_travelled)

def rest():
  possible_health_gains = [5, 5, 5, 10, 10, 10, 10, 15, 15, 20]
  index = random.randint(0,9)
  health_gain = possible_health_gains[index]
  print(f"You gained {health_gain} in health.")
  return(health_gain)

def buy():
  global food
  global wheels
  global oxen
  global clothes
  purchase = random.randint(1, 8)
  if purchase == 1:
    oxen += 1
    money_spent = 20
    print("You spent $20 on 1 ox.")
  if purchase == 2:
    clothes += 1
    money_spent = 10
    print("You spent $10 on 1 set of clothing.")
  if purchase == 3:
    wheels += 1
    money_spent = 10
    print("You spent $10 on 1 wheel.")
  if purchase == 4:
    food += 100
    money_spent = 20
    print("You spent $20 on 100 lbs of food.")
  if purchase == 5:
    oxen += 2
    money_spent = 40
    print("You spent $40 on 2 oxen.")
  if purchase == 6:
    clothes += 2
    money_spent = 20
    print("You spent $20 on 2 sets of clothing.")
  if purchase == 7:
    wheels += 2
    money_spent = 20
    print("You spent $20 on 2 wheels.")
  if purchase == 8:
    food += 200
    money_spent = 40
    print("You spent $40 on 200 lbs of food.")
  return(money_spent)

def hunt():
  possible_food_gains = [0, 20, 40, 60, 80, 100]
  index = random.randint(0,5)
  food_gain = possible_food_gains[index]
  print(f"You gained {food_gain} lbs of food.")
  return(food_gain)

intro()
while game == True:
  option = choose_an_option(days)
  if option == "1":
    distance -= travel()
  elif option == "2":
    health += rest()
  elif option == "3":
    money -= buy()
  elif option == "4":
    food += hunt()
  days += 1
