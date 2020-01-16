import pygame
import time
import random

health = 150
typhoid = False
cholera = False
dysentery = False
measles = False
days = 0
distance = 2000
food = 800
wheels = 8
oxen = 8
clothes = 8
money = 800
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
              print("That's not valid, try again. Please only use letters in writing your name.")
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
  if health >= 100:
    print(f"Health: Good ({health})")
  elif 100 > health >= 74:
    print(f"Health: Fair ({health})")
  else:
    print(f"Health: Poor ({health})")
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

def choose_an_option():
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
      elif oxen == 0:
        distance_travelled = 1
      else:
        distance_travelled = random.randint(5, 7)
  if what_to_judge_travel_by == 3:
      if wheels >=4:
        distance_travelled = random.randint(12, 18)
      elif wheels == 0:
        distance_travelled = 1
      else:
        distance_travelled = random.randint(5, 11)
  print(f"You travelled {distance_travelled} miles.")
  return(distance_travelled)

def rest():
  global typhoid
  global cholera
  global dysentery
  global measles
  global diseases
  possible_health_gains = [5, 5, 5, 10, 10, 10, 10, 15, 15, 20]
  index = random.randint(0,9)
  health_gain = possible_health_gains[index]
  print(f"You gained {health_gain} in health.")

  if diseases != []:
    recover_disease = random.randint(1,4)
    if recover_disease == 2:
      if typhoid == True:
        print("You recovered from typhoid.")
        typhoid = False
        diseases.remove("typhoid")
        health_gain += 25
      elif measles == True:
        print("You recovered from the measles.")
        measles = False
        diseases.remove("measles")
        health_gain += 25
      elif dysentery == True:
        print("You recovered from dysentery.")
        dysentery = False
        diseases.remove("dysentery")
        health_gain += 25
      elif cholera == True:
        print("You recovered from cholera.")
        cholera = False
        diseases.remove("cholera")
        health_gain += 25
  return(health_gain)

def buy():
  global food
  global wheels
  global oxen
  global clothes
  purchase = random.randint(1, 8)
  if purchase == 1 and money >= 20:
    oxen += 1
    money_spent = 20
    print("You spent $20 on 1 ox.")
  elif purchase == 2 and money >= 10:
    clothes += 1
    money_spent = 10
    print("You spent $10 on 1 set of clothing.")
  elif purchase == 3 and money >= 10:
    wheels += 1
    money_spent = 10
    print("You spent $10 on 1 wheel.")
  elif purchase == 4 and money >= 20:
    food += 100
    money_spent = 20
    print("You spent $20 on 100 lbs of food.")
  elif purchase == 5 and money >= 40:
    oxen += 2
    money_spent = 40
    print("You spent $40 on 2 oxen.")
  elif purchase == 6 and money >= 20:
    clothes += 2
    money_spent = 20
    print("You spent $20 on 2 sets of clothing.")
  elif purchase == 7 and money >= 20:
    wheels += 2
    money_spent = 20
    print("You spent $20 on 2 wheels.")
  elif purchase == 8 and money >= 40:
    food += 200
    money_spent = 40
    print("You spent $40 on 200 lbs of food.")
  else:
    print("You don't have enough money to make a purchase today. What a waste of a day.")
    money_spent = 0
  return(money_spent)

def hunt():
  possible_food_gains = [80, 0, 80, 90, 20, 100, 40, 60, 80, 100, 100]
  index = random.randint(0,10)
  food_gain = possible_food_gains[index]
  print(f"You gained {food_gain} lbs of food.")
  return(food_gain)

def eat():
  if health >= 75:
    food_eaten = random.randint(13, 17)
  elif 75 > health >= 50:
    food_eaten = random.randint(15, 20)
  else:
    food_eaten = random.randint(17, 25)
  if food < food_eaten:
    food_eaten = food
  print(f"During the day, you ate {food_eaten} pounds of food.")
  return(food_eaten)

def sick():
  global typhoid
  global cholera
  global dysentery
  global measles
  global diseases
  global health
  get_disease = random.randint(0,10)
  if get_disease == 1 or get_disease == 5:
    disease_gotten = random.randint(1,4)
    if disease_gotten == 1 and typhoid == False:
      print("You have fallen ill with typhoid.")
      typhoid = True
      diseases.append("typhoid")
      health -= 30
    elif disease_gotten == 2 and cholera == False:
      print("You have fallen ill with cholera.")
      cholera = True
      diseases.append("cholera")
      health -= 30
    elif disease_gotten == 3 and dysentery == False:
      print("You have fallen ill with dysentery.")
      dysentery = True
      diseases.append("dysentery")
      health -= 30
    elif disease_gotten == 4 and measles == False:
      print("You have fallen ill with the measles.")
      measles = True
      diseases.append("measles")
      health -= 30
  return

def thief():
  global food
  global wheels
  global oxen
  global clothes
  global money
  chance_of_thief = random.randint(0,10)
  if chance_of_thief == 6 or chance_of_thief == 9:
    item_stolen = random.randint(1,5)
    amount_stolen = random.randint(1,4)
    if item_stolen == 1 and food > 0:
      if amount_stolen == 1 and food > 300:
        print("Thieves have come at night to steal 300 lbs of food.")
        food -= 300
      elif amount_stolen == 2 and food > 200:
        print("Thieves have come at night to steal 200 lbs of food.")
        food -= 200
      elif amount_stolen == 3 and food > 100:
        print("Thieves have come at night to steal 100 lbs of food.")
        food -= 100
      elif amount_stolen == 4 and food > 50:
        print("Thieves have come at night to steal 50 lbs of food.")
        food -= 50
      else:
        print("Thieves have come at night to steal all of your food.")
        food = 0
    if item_stolen == 2 and wheels > 0:
      if amount_stolen == 1 and wheels > 1:
        print("Thieves have come at night to steal 1 wheel.")
        wheels -= 1
      elif amount_stolen == 2 and wheels > 2:
        print("Thieves have come at night to steal 2 wheels.")
        wheels -= 2
      elif amount_stolen == 1 and wheels > 1:
        print("Thieves have come at night to steal 1 wheel.")
        wheels -= 1
      elif amount_stolen == 4 and wheels > 2:
        print("Thieves have come at night to steal 2 wheels.")
        wheels -= 2
      else:
        print("Thieves have come at night to steel all of your wheels.")
        wheels = 0
    if item_stolen == 3 and oxen > 0:
      if amount_stolen == 1 and oxen > 1:
        print("Thieves have come at night to steal 1 ox.")
        oxen -= 1
      elif amount_stolen == 2 and oxen > 2:
        print("Thieves have come at night to steal 2 oxen.")
        oxen -= 2
      elif amount_stolen == 3 and oxen >3:
        print("Thieves have come at night to steal 3 oxen.")
        oxen -=3
      elif amount_stolen == 4 and oxen > 2:
        print("Thieves have come at night to steal 2 oxen.")
        oxen -= 2
      else:
        print("Thieves have come at night to steel all of your oxen.")
        oxen = 0
    if item_stolen == 4 and clothes > 0:
      if amount_stolen == 1 and clothes >2:
        print("Thieves have come at night to steal 2 sets of clothing.")
        clothes -= 2
      elif amount_stolen == 2 and clothes > 1:
        print("Thieves have come at night to steal 1 set of clothing.")
        clothes -= 1
      elif amount_stolen == 3 and clothes > 1:
        print("Thieves have come at night to steal 1 set of clothing.")
        clothes -= 1
      elif amount_stolen == 4 and clothes > 2:
        print("Thieves have come at night to steal 2 sets of clothing.")
        clothes -= 2
      else:
        print("Thieves have come at night to steal all of your clothing.")
        clothes = 0
    if item_stolen == 5 and money > 0:
      if amount_stolen == 1 and money > 100:
        print("Thieves have come at night to steal $100.")
        money -= 100
      elif amount_stolen == 2 and money > 80:
        print("Thieves have come at night to steal $80.")
        money -= 80
      elif amount_stolen == 3 and money > 70:
        print("Thieves have come at night to steal $70.")
        money -= 70
      elif amount_stolen == 4 and money > 50:
        print("Thieves have come at night to steal $50.")
        money -= 50
      else:
        print("Thieves have come at night to steal all of your money.")
        money = 0
  return

def reevaluate_health():
  health_decrease = 0

  if len(diseases) == 1:
    health_decrease += 2
  elif len(diseases) == 2:
    health_decrease += 3
  elif len(diseases) == 3:
    health_decrease += 5
  elif len(diseases) == 4:
    health_decrease += 8
  
  if food == 0:
    health_decrease += 15
  elif food < 50:
    health_decrease += 5
  elif food < 100:
    health_decrease += 3
  elif food < 150:
    health_decrease += 1
  
  if clothes == 0:
    health_decrease += 10
  elif clothes < 3:
    health_decrease += 2
  
  if health < health_decrease:
    health_decrease = health
  return(health_decrease)

def continue_game():
  if health <= 0:
    return False
  if days == 259:
    return False
  if distance == 0:
    return False
  else:
    return True


intro()
while game == True:
  option = choose_an_option()
  if option == "1":
    distance -= travel()
  elif option == "2":
    health += rest()
  elif option == "3":
    money -= buy()
  elif option == "4":
    food += hunt()
  health -= reevaluate_health()
  food -= eat()
  sick()
  thief()
  days += 1
  game = continue_game()

if distance == 0:
  print("You won! You made it to Oregon before December 15th. Congratulations, and enjoy your life out west!")
elif health <= 0:
  print(f"You died on the trail, maybe due to disease or due to lack of proper food and clothing.")
  print(f"You had {food} pounds of food left, {clothes} sets of clothing, and you were suffering from {len(diseases)} disease(s).")
elif days == 259:
  print("You made it as far as you could, but winter has fallen and you are too ill-equipped to travel, so you died on the trail.")