import random, sys, os, keyboard, subprocess, time

################
# Introduction #
################
def introduction():
    check = 1
    while check == 1:
        print()
        print("WELCOME TO DRAGONS ADVENTURE! Seems like you are the choosen one to defeat the enemies that been destroying our village.")
        print("Yeah, nobody wanted the dirty work...（￣へ￣）")
        print()
        proceed = (input("Would you like to meet your party and enemies? Y/N: "))
        if proceed  in ["N","n"]:
            print ("Well, you don't really got a choice, let's continue ;)")
        elif proceed in ["Y","y"]:
            print ("Great, let's get started!")
        else:
            print()
            print ("You are so unpredictable")
        time.sleep(1)
        check = 0

#####################
# Characters Status #
#####################

class char_stats: #Creates a class with all necessary stats for the code to run properly
    def __init__(stat, name, max_hp, hp, max_mp, mp, ap, wp, init, d20):
        stat.name = name
        stat.hp = hp 
        stat.max_hp = max_hp
        stat.mp = mp
        stat.max_mp = max_mp 
        stat.ap = ap
        stat.wp = wp
        stat.init = init
        stat.d20 = d20

def name_into_variable(name): #this function converts a character's name into it's variable so other functions can work 
        if name == "priest":
            return priest
        elif name == "warrior":
            return warrior
        elif name == "orc":
            return orc
        elif name == "goblin":
            return goblin
        elif name == "kobold":
            return kobold
        elif name == "hobgoblin":
            return hobgoblin

def all_characters(): #Creates several characters with stats in the following order: Name, Max HP, Current HP, MP, AP, WP, init and diceroll (for the initiative function)
    #Character stats in function so it's easier to restart the stats to their initial values on a new game
    global warrior, priest, orc, goblin, hobgoblin, kobold

    warrior = char_stats("warrior", 32, 32, 10, 10, 2, 5, 2, 0) 

    priest = char_stats("priest", 20, 20, 25, 25, 0, 2, 6, 0) 

    orc = char_stats("orc", 15, 15, 0, 0, 1, 4, 2, 0)

    goblin = char_stats("goblin", 14, 14, 0, 0, 1, 4, 2, 0)

    hobgoblin = char_stats("hobgoblin", 13, 13, 0, 0, 1, 4, 2, 0)

    kobold = char_stats("kobold", 12, 12, 0, 0, 1, 4, 2, 0)

enemy = ("orc", "goblin", "hobgoblin" , "kobold")

ally = ("warrior", "priest")

class item:
    def __init__(self, uses):
        self.uses = uses

crystal = item(1)
mana_potion = item(1)
revive = item(1)

####################
# Combat Mechanics #
####################

atk_words = ["atk","Atk", "attack", "Attack"]

magic_words = ["mag", "Mag", "magic", "Magic"]

item_words = ["itm", "Itm", "item", "Item"]

rush_desc = "Rushdown: Rushes into the enemy, tackling them into the ground. Inflicts between 6 and 9 damage. Costs 5 mana.\n"

exor_desc = "Exorcism: Corrupt and enemy's life essence. Inflicts between 2 and 8 damage. Costs 5 mana.\n"

mend_desc = "Mend: Repay some of a character's current debt to the Death god. Heals a character between 3 and 8. Costs 3 mana.\n"

round_num = 1

###############
# Combat Zone #
###############
def end_action(): #This makes so the code only continues when the down arrow is pressed and updates the ui
        time.sleep(1)
        print()
        print("Press Down Arrow to Proceed")
        while keyboard.is_pressed('down') != True:
            pass
        ui()

def item_showcase():
    global end_action
    print()
    print ("Oh right! Before you start fighting, you can also use some items in your inventory to help your character's status in combat!（ミ￣ー￣ミ）")
    print ("I will quickly show you your available items.")
    print()
    print(f"{crystal.uses} Crystal (+2 Attack)\n{mana_potion.uses} Mana potion (+10 MP)\n{revive.uses} Revive")
    end_action()

def alive(): #Checks if characters are alive, ends game if all allies or all enemies are dead
    global alive_char, dead_allies, dead_enemies
    chars = [warrior, priest, orc, goblin, hobgoblin, kobold]
    alive_char = []
    dead_allies = []
    dead_enemies = []
    for char in chars:
        if char.hp > 0:
            alive_char.append(char)
        else:
            char.hp = 0
            if char.name in enemy:
                dead_enemies.append(char.name)
            if char.name in ally:
                dead_allies.append(char.name)

    if len(dead_allies) == len(ally):
        ans = input(f"All allies have been slain.\nWould you like to play again? (Y/N)\n")
        end(ans)
    elif len(dead_enemies) == len(enemy):
        ans = input(f"All enemies have been slain.\nWould you like to play again? (Y/N)\n")
        end(ans)

def ui(): #UI function, prints alive characters separated from dead ones
    clearconsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    clearconsole() #clears the console so it doesn't get cluttered

    alive() 
    print(f"Round {round_num}")
    #Checks every character alive state and either prints their stats or marks them as dead
    for character in enemy:
        character = name_into_variable(character)
        if character in alive_char:
            print(f"\nEnemy: {character.name} Hp: {character.hp} Armor: {character.ap} Attack: {character.wp}")
    if len(dead_enemies) > 0:
        print(f"\nDead enemies:",*dead_enemies) #prints all elements from the list of dead enemies
    for character in ally:
        character = name_into_variable(character) 
        if character in alive_char:
            print(f"\nAlly:{character.name} Hp:{character.hp} MP:{character.mp} Armor:{character.ap} Attack:{character.wp}")
    if len(dead_allies) > 0:
        print(f"Dead allies:",*dead_allies)
    

def initiative(): #Rolls a dice for each character and sorts them in order of most to least initiative
    global atkorder

    def d20(): # Code based on answer by user jws1 on StackOverflow. (https://stackoverflow.com/questions/60193710/python-d20-dice-rolling-program)
        total = 0
        total += random.randint(1,20)
        return total

    for char in alive_char:
        char.d20 = d20() + char.init
        atkorder = alive_char #this happens so the list of alive characters doesn't get sorted out of its original order
        atkorder.sort(key=lambda x: (x.d20), reverse = True) # Code based on answer by user Art on StackOverflow (https://stackoverflow.com/questions/67750705/python-sorting-based-on-class-attribute)
    
 
#################
# Main function #
#################

def Round(): #Gets a character from the initiative order and calculates its actions.

    global round_num, end_action

    def dmg_calc(attacking, defending):
        dmg_fin = attacking.wp - defending.ap
        if dmg_fin < 0:
            dmg_fin = 0
        return int(dmg_fin)

    def d4():
        total = 0
        total += random.randint(1,4)
        return total

    def d6():
        total = 0
        total += random.randint(1,6)
        return total

    def rushdown(attacking, defending):
        nonlocal check

        try:
            if defending.name in enemy and defending in alive_char: #checks if target is an enemy and is alive
                dmg = attacking.wp + d4()
                defending.hp = defending.hp - dmg
                attacking.mp += -5
                check = 0
                print(f"The {attacking.name} rushed into the {defending.name} and delt {dmg} damage")
                end_action() #stops code until user wishes to proceed and then refreshes ui
            else:
                print("Chosen target not valid.\n")
        except:
            print("Chosen target not valid.\n")
        
    def exorcism(attacking, defending):
        nonlocal check

        try:
            if defending.name in enemy and defending in alive_char: #checks if target is an enemy and is alive
                dmg = d4() * 2
                defending.hp = defending.hp - dmg
                print(f"The {attacking.name} exorcised the {defending.name} and delt {dmg} damage")
                check = 0
                end_action() #refreshes ui and stops code until user wishes to proceed
            else:
                print("Chosen target not valid.\n")
        except:
            print("Chosen target not valid.\n")

    def mend(healer, healed):
        nonlocal check
        try:
            if target.name in ally and target in alive_char:  #checks if target is an ally and is alive
                heal = healer.wp + d6()
                if healed.max_hp < healed.hp + heal:
                    healed.hp = healed.max_hp
                else:
                    healed.hp = healed.hp + heal
                check = 0
                end_action() #refreshes ui and stops code until user wishes to proceed
            else:
                print("Chosen target not valid.\n")
        except:
            print("Chosen target not valid.\n")

    def item_use():
        nonlocal check
        print(f"Available items:\n{crystal.uses} Crystal (+2 Attack)\n{mana_potion.uses} Mana potion (+10 MP)\n{revive.uses} Revive")
        item = input(f"\nWhat item do you want to use?\n")
        target = input(f"\nWhom do you want to use it on?\n")
        target = name_into_variable(target)
        try:
            if item == "Crystal" or item == "crystal":
                if target in alive_char and target.name in ally:
                    if crystal.uses > 0:
                        target.wp += 2
                        crystal.uses += -1
                        check = 0
                        print(f"{target.name} was powered up and has +2 attack.")
                        end_action() #refreshes ui and stops code until user wishes to proceed
                    else:
                        print(f"No {item}s left to use.\n")
                else:
                    print(f"Chosen target not valid \n")

            if item == "Mana potion" or item == "mana potion" or item == "mana" or item == "Mana":
                if target in alive_char and target.name in ally:
                    if mana_potion.uses > 0:
                        target.mp += 10
                        if target.mp > target.max_mp:
                            target.mp = target.max_mp
                        mana_potion.uses += -1
                        check = 0
                        print(f"{target.name} has restored 10 MP")
                        end_action() #refreshes ui and stops code until user wishes to proceed
                    else:
                        print(f"No {item}s left to use.\n")
                else:
                    print(f"Chosen target not valid\n")

            if item == "Revive" or item == "revive":
                if target in dead_allies and target in ally.name:
                    if revive.uses > 0:
                        target.hp == target.max_hp
                        revive.uses += -1
                        check = 0
                        print(f"{target.name} has been revived\n")
                        end_action() #refreshes ui and stops code until user wishes to proceed
                    else:
                        print(f"No {item}s left to use.")
                else:
                    print(f"Chosen target not valid\n")    
            else:
                print(f"Chosen item not valid\n")    
        except:
            print(f"Chosen target not valid\n") 
            
    for char in atkorder: #Selects each character in order of initiative
        name_char = char.name #gets the character name so the rest of the code can identify which character it is refering to
        check = 1 # this check exists so the code can know when the current character has finished its turn

        print(f"\nThe {name_char} is preparing to act\n")
        time.sleep(1)
        print("press down arrow to proceed")
        while True:
            if keyboard.is_pressed('down'):
                break
        if name_char in enemy: #if selected character is an enemy just calculates its dmg
            while check == 1:
                chosen =  random.choice(ally) #chooses randomly one allied character to attack
                chosen = name_into_variable(chosen)
                if chosen in alive_char:
                    chosen.hp = chosen.hp - dmg_calc(char, chosen)
                    print(f"\nEnemy {name_char} attacked allied {chosen.name} and dealt {dmg_calc(char, chosen)} damage.")
                    check = 0
                    end_action()
                
        elif name_char in ally: #if selected character is an ally it enters the action screen
            while check == 1:
                print(f"\nIt's time for the {name_char} to do an action!\nWhat should the {name_char} do?\nThe {name_char} can either Attack, use an item or cast Magic")
                action = input()

                if action in atk_words: #Attack action was chosen
                    target = input(f"\nWhich enemy should {name_char} attack?\n")
                    target = name_into_variable(target)
                    try:
                        if target.name in enemy and target in alive_char: #Checks if targeted character is an enemy and is alive
                            target.hp = target.hp - dmg_calc(name_into_variable(name_char), target)
                            print(f"\nThe allied {name_char} attacked enemy {target.name} and dealt {dmg_calc(char, target)} damage.")
                            end_action() #refreshes ui and stops code until user wishes to proceed
                            check = 0
                        else:
                            print(f"\nChosen target not valid.\n")
                    except:
                        print("Chosen target not valid.\n")    

                elif action in magic_words: #Magic action was chosen
                    print(f"The alied {name_char} can cast the following magic:\n")

                    if char == warrior:  #checks if current character is a warrior
                        print(rush_desc)
                        if char.mp >= 5:
                            target = input(f"Who do you want to attack?\n")
                            target = name_into_variable(target)
                            rushdown(char, target)
                        else:
                            print("Not Enough Mana")

                    elif char == priest: #checks if current character is a priest
                        print(f"{exor_desc}\n{mend_desc}")
                        spell = input(f"Which spell do you want to use?\n")

                        if spell == "Exorcism" or spell == "exorcism":
                            if char.mp >= 5:
                                target = input(f"Who do you want to attack?\n")
                                target = name_into_variable(target)
                                exorcism(char, target)
                                
                            else:
                                print("Not Enough Mana")

                        elif spell == "Mend" or spell == "mend":
                            if char.mp >= 3:
                                target = input(f"Who do you want to heal?\n")
                                target = name_into_variable(target)
                                mend(char, target)
                                end_action() #refreshes ui and stops code until user wishes to proceed
                            else:
                                print("Not Enough Mana")
                elif action in item_words: #items were chosen
                    item_use()
                else:
                    print("The character cant do that action.")

        else:
            print("Something not intended happened.")
    round_num += 1

def end(answer): #At the end of the game it either restarts the game or closes the program
        if answer == "y" or answer == "Y":
            #This bit of code creates a second game without closing the console and closes the first game so it doesn't show up if you finish the seccond game
            subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:]) # Original code found at https://maschituts.com/how-to-restart-a-program-in-python-explained/
            sys.exit() #without this, when the second game created above was closed, the first game would appear again and rerun itself
        elif answer == "n" or answer == "N":
            sys.exit()

def game():
    all_characters()
    introduction()
    item_showcase()
    while True:
        ui()
        alive()
        initiative()
        Round()

game()