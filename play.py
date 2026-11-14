import time
import random
from game_logic import Kingdom, EnemyKingdom, s_print, pause

s_print("Welcome to Warriors and Wizards")
pause(2)
print("\nYou wake up from a long sleep for another day of training your sword skills")
pause(6)
print("\nWord is spreading around the kingdom quickly")
pause(3)
s_print("\nYour king has been killed in battle trying to regain the lost territory of your kingdom.\nYou are next up in line.")
pause(3)
ruler = input("\nWhat is your name:")
s_print(f"\nWelcome, {ruler}. Your kingdom prepares for war...\n")
pause(2)
print(f"\nRuler {ruler} Your kingdom was once a thriving nation, but a civil war has broken out for the last 10 years due to resource managment, spliting the kingdom into 4 territories.")
pause(6)
print("\nYou control 1 of the 4 new territories. Your goal is to reclaim the lost land by building your new army that will consist of warriors and wizards.")
pause(6)
print("\nSome left over gold and food is all you have left from the previous kings resources.")
pause(5)
print("\nWhen building your army keep in mind that warriors have more strength then wizards, but wizards have more intelligence then warriors.")
s_print("\nBoth are needed to win in battle. Make sure they are kept well fed and declare war on enemy kingdom to gain gold upon victory.")
pause(1)
print("\nThe remaing 3 territories are")
pause(2)
s_print("\nToronto Empire, Ottawa Kingdom, Montreal Realm")
pause(6)

player_kingdom = Kingdom()

# Creating 3 enemy kingdoms
enemy_names = ["Toronto Empire", "Ottawa Kingdom", "Montreal Realm"]
enemy_kingdoms = []
for name in enemy_names:
    enemy_kingdoms.append(EnemyKingdom(name, gold = random.randint(20,40)))

turns = 0

#Game runs untill all enemies defeated or player loses
while enemy_kingdoms:
    print(f"\n --- Turn {turns +1} ---")
    player_kingdom.show_army()

    if turns == 1:
        s_print("\nYour scouts report enemy movements nearby build up your army quick.\n")
    elif turns == 2:
        s_print("\nYour advisors urge you to strengthen your forces and train your units.\n")
    elif turns == 4:
        s_print("\nThe time to reclaim lost lands is near.\n")

    print("Options:")
    print("1. Recruit Warrior (15 gold)")
    print("2. Recruit Wizard (15 gold)")
    print("3. Train a unit (10 gold)")
    print("4. Buy food (10 gold = 3 food)")
    print("5. Feed your army")
    print("6. Attack an enemy kingdom")

    choice = input("Choose an action wisely (1-6): ")

    if choice == "1":
        player_kingdom.buy_unit("warrior")
    elif choice == "2":
        player_kingdom.buy_unit("wizard")
    elif choice == "3":
        player_kingdom.train_unit()
    elif choice == "4":
        if player_kingdom.gold >= 10:
            player_kingdom.gold -= 10
            player_kingdom.food += 3
            print("Bought 3 food.")
        else:
            print("Not enough gold!")
    elif choice == "5":
        player_kingdom.feed_army()
    elif choice == "6":
        if not enemy_kingdoms:
            print("All enemies defeated!")
            break
        enemy = random.choice(enemy_kingdoms)
        s_print(f"You march your army to face {enemy.name}.\n")
        player_power = sum((u.strength + u.intelligence) for u in player_kingdom.units if u.fed)
        enemy_power = enemy.full_power()
        print(f"Your Power: {player_power} | Enemy Power: {enemy_power}")

        if player_power >= enemy_power:
            loot = random.randint(10, 30)
            s_print(f"Victory! You defeated {enemy.name} and looted {loot} gold.\n")
            pause(2)
            print(f"You now rule {enemy.name} as well!")
            player_kingdom.gold += loot
            enemy_kingdoms.remove(enemy)
        else:
            print("The battle is fierce and goes on for days.")
            pause(3)
            s_print("Your losing units...")
            s_print("Your units are not strong enough...")
            pause(3)
            s_print(f"\nDefeat! You lost to {enemy.name}.\n")
            for unit in player_kingdom.units:
                s_print(f"{unit.name} has fallen in battle.\n")
            s_print("The kingdom mourns your loss. Your territory is concquered as you surrender to the Enemy.\nGame over.\n")
            break
    else:
        print("Invalid option.")

    player_kingdom.update_hunger(turns)
    turns += 1
    pause(2)



if not enemy_kingdoms:
    s_print(f"\nCongratulations, {ruler}! You have reclaimed all lost territories and secured your kingdom's future!\n")
    print("Thank you for playing!")

