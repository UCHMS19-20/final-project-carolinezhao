import pygame
import time
import random

pygame.init()

def load_ox_image(name):
  """Loads an image for the ox animation and scales it properly. Returns the image"""
  image = pygame.image.load(name)
  image = pygame.transform.scale(image, (240, 100))
  return image
def load_talking_image(name):
  """Loads an image for the talking animation and scales it properly. Returns the image"""
  image = pygame.image.load(name)
  image = pygame.transform.scale(image, (325, 500))
  return image
def load_hunting_image(name):
  """Loads an image for the hunting animation and scales it properly. Returns the image"""
  image = pygame.image.load(name)
  image = pygame.transform.scale(image, (750, 261))
  return image
def load_resting_image(name):
  """Loads an image for the resting animation and returns it"""
  image = pygame.image.load(name)
  return image

class oxSprite(pygame.sprite.Sprite):
    '''Based on a code written by a Stack Overflow user regarding animation through Pygame'''
    def __init__(self):
        """Loads the necessary images in the animation into a list (self.images)"""
        super(oxSprite, self).__init__()
        self.images = []
        self.images.append(load_ox_image(r"src\img\ox1.png"))
        self.images.append(load_ox_image(r"src\img\ox3.png"))
        self.images.append(load_ox_image(r"src\img\ox2.png"))
        self.images.append(load_ox_image(r"src\img\ox3.png"))

        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(540, 300, 240, 100)
    def update(self):
        '''This method iterates through the elements inside self.images and displays the next one each tick'''
        self.index += 1
        time.sleep(0.3)
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
class talkingSprite(pygame.sprite.Sprite):
    '''Based on a code written by a Stack Overflow user regarding animation through Pygame'''
    def __init__(self):
        """Loads the necessary images in the animation into a list (self.images)"""
        super(talkingSprite, self).__init__()
        self.images = []
        self.images.append(load_talking_image(r"src\img\talking1.png"))
        self.images.append(load_talking_image(r"src\img\talking2.png"))
        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(237.5, 100, 325, 500)
    def update(self):
        '''This method iterates through the elements inside self.images and displays the next one each tick'''
        self.index += 1
        time.sleep(0.3)
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
class huntingSprite(pygame.sprite.Sprite):
    '''Based on a code written by a Stack Overflow user regarding animation through Pygame'''
    def __init__(self):
        """Loads the necessary images in the animation into a list (self.images)"""
        super(huntingSprite, self).__init__()
        self.images = []
        self.images.append(load_hunting_image(r"src\img\hunting1.png"))
        self.images.append(load_hunting_image(r"src\img\hunting2.png"))
        self.images.append(load_hunting_image(r"src\img\hunting3.png"))
        self.images.append(load_hunting_image(r"src\img\hunting4.png"))
        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(25, 139, 750, 288)
    def update(self):
        '''This method iterates through the elements inside self.images and displays the next one each tick'''
        self.index += 1
        time.sleep(0.2)
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
class restingSprite(pygame.sprite.Sprite):
    '''Based on a code written by a Stack Overflow user regarding animation through Pygame'''
    def __init__(self):
        """Loads the necessary images in the animation into a list (self.images)"""
        super(restingSprite, self).__init__()
        self.images = []
        self.images.append(load_resting_image(r"src\img\resting1.png"))
        self.images.append(load_resting_image(r"src\img\resting2.png"))
        self.images.append(load_resting_image(r"src\img\resting3.png"))
        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(227.5, 100, 345, 480)
    def update(self):
        '''This method iterates through the elements inside self.images and displays the next one each tick'''
        self.index += 1
        time.sleep(0.4)
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

# Defining pygame-related variables regarding displays, fonts, and sprites.
dayFont = pygame.font.SysFont('Courier New', 100)
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Oregon Trail')
ox_sprite = oxSprite()
ox_group = pygame.sprite.Group(ox_sprite)
talking_sprite = talkingSprite()
talking_group = pygame.sprite.Group(talking_sprite)
hunting_sprite = huntingSprite()
hunting_group = pygame.sprite.Group(hunting_sprite)
resting_sprite = restingSprite()
resting_group = pygame.sprite.Group(resting_sprite)

# Defining the variables that are stats to judge how the player is doing during the game.
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
  """An animated character explains the premise of the Oregon Trail Game to the player
  Also asks for a name of the player (not to be used again, just for one line of personalization)"""
  for x in range (0, 10):
    talking_group.update()
    talking_group.draw(screen)
    pygame.display.flip()
    screen.fill((25,25,25))
  print("Hi. Welcome to the Oregon Trail.")
  time.sleep(1)
  for x in range (0, 5):
    talking_group.update()
    talking_group.draw(screen)
    pygame.display.flip()
    screen.fill((25,25,25))
  name = ""
  while name == "":
      name = input("What is your name? ")
      for n in name.lower():
          if n not in "abcdefghijklmnopqrstuvwxyz":
              for x in range (0, 5):
                talking_group.update()
                talking_group.draw(screen)
                pygame.display.flip()
                screen.fill((25,25,25))
              print("That's not valid, try again. Please only use letters in writing your name.")
              name = ""
              break
  for x in range (0, 4):
    talking_group.update()
    talking_group.draw(screen)
    pygame.display.flip()
    screen.fill((25,25,25))
  print(f"Hello {name.title()}.")
  time.sleep(.3)
  for x in range (0, 10):
    talking_group.update()
    talking_group.draw(screen)
    pygame.display.flip()
    screen.fill((25,25,25))
  print("Right now, we are in Independence, Missouri.")
  time.sleep(.3)
  for x in range (0, 10):
    talking_group.update()
    talking_group.draw(screen)
    pygame.display.flip()
    screen.fill((25,25,25))
  print("You want to go out west, and the Oregon Trail is the best way to do so.")
  time.sleep(.3)
  for x in range (0, 10):
    talking_group.update()
    talking_group.draw(screen)
    pygame.display.flip()
    screen.fill((25,25,25))
  print("Today is April 1st. Your goal is to make it to Oregon before December 15, when winter will fall.")
  time.sleep(.3)
  for x in range (0, 10):
    talking_group.update()
    talking_group.draw(screen)
    pygame.display.flip()
    screen.fill((25,25,25))
  print("It's a dangerous journey, but I have faith in you. Good luck!")
  time.sleep(2)
  return

def status():
  """Print out the player's stats and generally inform them on them how well they are doing"""
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
  """Displays a sign showing the day of the trip for the player to keep track
  Also uses the status() function to inform the player of their stats
  Asks the player what action they would like to take that day, returns the option the player chooses"""
  print("\n")
  time.sleep(1)
  print(f"This is day {1+days} of your trip.")
  image = pygame.image.load(r"src\img\DaySign.png")
  screen.blit(image, (182.5, 240))
  dayNumber = dayFont.render("DAY:" + str(days+1), False, (253, 205, 146))
  screen.blit(dayNumber,(200,270))
  pygame.display.update()
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
      screen.fill((25, 25, 25))
      pygame.display.update
      return option 

def travel():
  """Randomly generates a distance travelled by judging the health, the oxen, or the wheels that the player currently has
  Animates an ox with a wagon walking before informing the player of the distance travelled
  Returns the distance travelled"""
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
  for x in range (0, 10):
    pygame.draw.rect(screen,(0,200,0),(0,400,800,200))
    ox_group.update()
    ox_group.draw(screen)
    pygame.display.flip()
    screen.fill((25,25,25))
    pygame.draw.rect(screen,(0,200,0),(0,400,800,200))
  print(f"You travelled {distance_travelled} miles.")
  return(distance_travelled)

def rest():
  """Randomly generates the amount of health gained (the amount to be added to a player's health status) and randomly determines if the player will recover from a sickness (if applicable)
  Animates a person sleeping and informs the player of any changes in the character's health
  Returns the health gain (to be added to the player's health stat)"""
  global typhoid
  global cholera
  global dysentery
  global measles
  global diseases
  for x in range (0, 11):
    pygame.draw.rect(screen,(0,200,0),(0,400,800,200))
    resting_group.update()
    resting_group.draw(screen)
    pygame.display.flip()
    screen.fill((25,25,25))
    pygame.draw.rect(screen,(0,200,0),(0,400,800,200))  
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
  """Randomly uses the player's money to buy an item if they have enough money
  Animates money flying away and informs the player of their purchase
  Returns the money spent"""
  money1 = pygame.image.load(r"src\img\money1.png")
  money2 = pygame.image.load(r"src\img\money1.png")
  x_coord = 0
  y_coord = 400
  for x in range (0, 11):
    screen.fill((25, 25, 25))
    screen.blit(money1, (x_coord,y_coord))
    screen.blit(money2, (x_coord+100,y_coord-100))
    pygame.display.update()
    time.sleep(.2)
    x_coord += 80
    y_coord -= 50
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
  """Randomly generates an amount of food gained from a day of hunting by the player
  Animates a moose being shot and informs the player of any changes in the food supply
  Returns the food gain"""
  possible_food_gains = [80, 0, 80, 90, 20, 100, 40, 60, 80, 100, 100]
  index = random.randint(0,10)
  food_gain = possible_food_gains[index]
  for x in range (0, 10):
    pygame.draw.rect(screen,(0,200,0),(0,400,800,200))
    hunting_group.update()
    hunting_group.draw(screen)
    pygame.display.flip()
    screen.fill((25,25,25))
    pygame.draw.rect(screen,(0,200,0),(0,400,800,200))  
  print(f"You gained {food_gain} lbs of food.")
  return(food_gain)

def eat():
  """Randomly generates an amount of food eaten depending on the player's health
  Informs the player of this number and returns the food eaten"""
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
  """Randomly determines if a person will get sick and what disease they get
  Informs the player if they have fallen ill and changes the illness stats as necessary"""
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
  """Randomly determines if a thief will come take supplies from the person and how much they will take
  Informs the player of their loss and changes the stats accordingly"""
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
  """Uses the player's stats to determine if their health decreases throughout the day
  Returns the decrease in health"""
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
  """Determines if the game should continue
  Will stop the game if the health is below 0, if the player has taken too long to reach their destination, or if the player has reached their destination
  Returns either false or true"""
  if health <= 0:
    return False
  if days >= 259:
    return False
  if distance <= 0:
    return False
  else:
    return True

intro()
while game == True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game = False

  screen.fill((25,25,25))

  # The player chooses what they would like to do, and the game calls on the function that corresponds to the player's choice
  option = choose_an_option()
  if option == "1":
    distance -= travel()
  elif option == "2":
    health += rest()
  elif option == "3":
    money -= buy()
  elif option == "4":
    food += hunt()
  time.sleep(1)

  # Resetting the screen to show the sign with the day number on it while the "nighttime" events happen (see below)
  screen.fill((25,25,25))
  image = pygame.image.load(r"src\img\DaySign.png")
  screen.blit(image, (182.5, 240))
  dayNumber = dayFont.render("DAY:" + str(days+1), False, (253, 205, 146))
  screen.blit(dayNumber,(200,270))
  pygame.display.update()
  time.sleep(1)

  # The game re-evaluates the player's stats and determines if any tragic events will happen to them at the end of the day/night
  health -= reevaluate_health()
  food -= eat()
  sick()
  thief()
  days += 1
  game = continue_game()

# Congratulatory message to be displayed the player wins the game by reaching Oregon
if distance <= 0:
  screen.fill((25,25,25))
  image = pygame.image.load(r"src\img\oregon.png")
  image = pygame.transform.scale(image, (800, 600))
  screen.blit(image, (0, 0))
  pygame.display.update()
  print("\n")
  print("You won! You made it to Oregon before December 15th. Congratulations, and enjoy your life out west!")

# Losing message to be displayed if the player dies by losing all their health
elif health <= 0:
  screen.fill((25,25,25))
  pygame.draw.rect(screen,(0,200,0),(0,400,800,200))
  image = pygame.image.load(r"src\img\tombstone.png")
  image = pygame.transform.scale(image, (490, 525))
  screen.blit(image, (155, 50))
  pygame.display.update()
  print("\n")
  print(f"You died on the trail, maybe due to disease or due to lack of proper food and clothing. Sorry.")
  print(f"You had {food} pounds of food left, {clothes} sets of clothing, and you were suffering from {len(diseases)} disease(s).")

# Losing message to be displayed if the player runs out of time and does not make it to the destination
elif days >= 259:
  screen.fill((25,25,25))
  pygame.draw.rect(screen,(0,200,0),(0,400,800,200))
  image = pygame.image.load(r"src\img\tombstone.png")
  image = pygame.transform.scale(image, (490, 525))
  screen.blit(image, (155, 50))
  pygame.display.update()
  print("\n")
  print("You made it as far as you could, but winter has fallen and you are too ill-equipped to travel, so you died on the trail. Sorry.")

time.sleep(20)
quit()
