import random
import time

# slowly printing something
def s_print(text):
    for i in text:
        print(i, end='', flush=True)
        time.sleep(0.1)

#getting a random number
#def roll(min,max):
    #return(randint(min,max))

# pausing a set amount
def pause(seconds):
    time.sleep(seconds)

# Warrior or Wizard start as set strenth, intelligence, and start as fed
class Unit:
    def __init__ (self, name, unit_type):
        self.name = name
        self.type = unit_type
        if self.type == "warrior":
            self.strength = 5
            self.intelligence = 3
        else:
            self.strength = 3
            self.intelligence = 5
        self.fed = True

# train units to gain strenth or intelligence
    def train(self):
        self.strength += 2
        self.intelligence +=2

# if hungry lose strenth an intelligence but only if it above 1
    def hungry(self):
        if self.strength >1:
            self.strength = self.strength - 1
        if self.intelligence >1:
            self.intelligence = self.intelligence -1

class EnemyKingdom:
    def __init__(self, name, gold):
        self.name = name
        self.gold = gold
        self.units = []
# creates a range for random ammounts of warriors in enemy kingdom
        for i in range(random.randint(1,2)):
            self.units.append(Unit(f"EnemyWarrior{i}", "warrior"))
# creates a range for random amounts of wizards in enemy kingdom
        for i in range(random.randint(1,2)):
            self.units.append(Unit(f"EnemyWizard{i}", "wizard"))

# function for getting totale power of an enemy kingdom
    def full_power(self):
        return sum(unit.strength + unit.intelligence for unit in self.units)

class Kingdom:
    def __init__(self):
        self.units = []
        self.gold = 60
        self.food = 5

# prints army stats and resources
    def show_army(self):
        print("\n Your Army ")
        for unit in self.units:
            print(f"{unit.name} {unit.type} - Stats: Strength: {unit.strength}, Intelligence: {unit.intelligence}, Fed: {'Yes' if unit.fed else 'No'}")
        print(f"Gold: {self.gold}, Food: {self.food}\n")

# buying a warrior or wizard
    def buy_unit(self, unit_type):
        if self.gold >=15:
            name = input("What is the name of your new unit: ")
            self.units.append(Unit(name, unit_type))
            self.gold -= 15
            print(f"{name} the {unit_type} has joined your army!")
        else:
            print("Not enough gold!")

# feeding army to keep hunger level up
    def feed_army(self):
        needed = len(self.units)
        if self.food >= needed:
            self.food -= needed
            for unit in self.units:
                unit.fed = True
            print("Your army is well fed and ready to fight!")
        else:
            s_print("Not enough food for everyone in your army! Remember, to maintain high morale make sure everyone can be fed when you feed your army, else no one eats. Your army is hungry, penalty applied.")
            for unit in self.units:
                unit.fed = False
                unit.hungry()
                s_print(f"{unit.name} has lost some stats due to hunger. ")

# gold calculations for training units and selecting random unit
    def train_unit(self):
        if not self.units:
            print("You have no units to train.")
            return
        if self.gold < 10:
            print("Not enough gold to train.")
            return
        self.gold -= 10
        unit = random.choice(self.units)
        unit.train()
        print(f"{unit.name} has trained and grown stronger and smarter!")

# updating units to be hungry after every 3 turns
    def update_hunger(self, turn_count):
        if turn_count % 4 == 0 and turn_count != 0 and self.units:
            s_print("Your army is getting hungry")
 # Only then update hunger
            for unit in self.units:
                if unit.fed == True:
                    unit.fed = False  # They were fed last time now unfed
                elif unit.fed == False:
                    unit.hungry()  # Already unfed now lose stats
                    s_print(f"{unit.name} is starving and has lost strength and intelligence!")
        else:
            pass
