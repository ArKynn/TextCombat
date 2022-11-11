import os
import random

################
# Introduction #
################

print("WELCOME TO DRAGONS ADVENTURE! Seems like you are the choosen one to defeat the enemies that been destroying our village.")
print("Yeah, nobody wanted the dirty work...（￣へ￣）")
print()
proceed = print(input("Would you like to meet your party and enemies? Y/N: "))
if proceed  == ("N", "n"):
    print ("Well, you don't really got a choice, let's continue ;)")
else: 
    print ("Great, let's get started!")


class char_stats:
    def __init__(stat, name, hp, mp, ap, wp, init, d20):
        stat.name = name
        stat.hp = hp 
        stat.mp = mp 
        stat.ap = ap
        stat.wp = wp
        stat.init = init
        stat.roll = d20

#####################
# Characters Status #
#####################
# Name, HP, MP, AP, WP, Init, dice roll

warrior = char_stats("warrior", 32, 5, 2, 5, 2, 0)

priest = char_stats("priest", 20, 25, 0, 2, 6, 0) 

orc = char_stats("orc", 15, 0, 2, 2, 2, 0) 

goblin = char_stats("goblin", 14, 0, 2, 2, 2, 0) 

hobgoblin = char_stats("hobgoblin", 13, 0, 2, 2, 2, 0) 

kobold = char_stats("kobold", 12, 0, 2, 2, 2, 0) 

enemy = [orc, goblin, hobgoblin, kobold] #list of enemy chars

ally = [warrior, priest] #list of allied chars

###################
# Combat Commands #
###################

atk_words = ["atk","Atk", "attack", "Attack"]

magic_words = ["mag", "Mag", "magic", "Magic"]

rushdown = ["Rushes into the enemy, tackling them into the ground. Inflicts between 6 and 9 damage. Costs 5 mana."]

exorcism = ["Corrupt and enemy's life essence. Inflicts between 2 and 8 damage. Costs 5 mana."]

mend = ["Repay some of a character's current debt to the Death God. Heals a character between 3 and 8. Costs 3 mana."]


###############
# Combat Zone #
###############

def ui(): #Basic ui (Might change later)
    clearconsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    clearconsole()

    print("Enemy: Orc                  Enemy: Goblin                   Enemy: Hobgoblin                           Enemy: Kobold")
    print(f"HP:{orc.hp}                 HP:{goblin.hp}                   HP:{hobgoblin.hp}                         HP:{kobold.hp}")
    print(f"MP:{orc.mp}                  MP:{goblin.mp}                    MP:{hobgoblin.mp}                       MP:{kobold.mp}")
    print(f"AP:{orc.ap}                  AP:{goblin.ap}                    AP:{hobgoblin.ap}                       AP:{kobold.ap}")
    print(f"WP:{orc.wp}                  WP:{goblin.wp}                    WP:{hobgoblin.wp}                       WP:{kobold.wp}")
    print(f"Init:{orc.init}                Init:{goblin.init}                  Init:{hobgoblin.init}                     Init:{kobold.init}")

    print(f"\n\n\n")
    print(f"Ally: Warrior               Ally: Priest")
    print(f"HP:{warrior.hp}                       HP:{priest.hp}")
    print(f"MP:{warrior.mp}                        MP:{priest.mp}")
    print(f"AP:{warrior.ap}                        AP:{priest.ap}")
    print(f"WP:{warrior.wp}                        WP:{priest.wp}")
    print(f"Init:{warrior.init}                      InitP:{priest.init}")

def alive(): #Checks if character is alive
    global alive
    chars = [warrior, priest, orc, goblin, hobgoblin, kobold]
    alive = []
    for char in chars:
        if char.hp > 0:
            alive.append(char)

def initiative(): #Rolls a dice for each character and sorts them in order of most to least initiative
    global atkorder

    def d20(): # Code based on answer by user jws1 on StackOverflow. (https://stackoverflow.com/questions/60193710/python-d20-dice-rolling-program)
        total = 0
        total += random.randint(1,20)
        return total

    for char in alive:
        char.d20 = d20() + char.init
        atkorder = sorted(alive, key=lambda x: (x.roll)) # Code based on answer by user falsetru on StackOverflow (https://stackoverflow.com/questions/26310394/python-sort-a-list-of-objects-based-on-their-attributes)
        print(atkorder)

def Round(): #Gets a character from the initiative order and calculate's its actions.
    def dmg_calc(attacking, defending):
        dmg_fin = defending.ap - attacking.wp
        if dmg_fin < 0:
            dmg_fin = 0

    def d4():
        total = 0
        total += random.randint(1,4)

    def d6():
        total = 0
        total += random.randint(1,6)

    def rushdown(attacking, defending):
        dmg = attacking.wp + d4
        dmg_fin = defending.ap - dmg
        if dmg_fin < 0:
            dmg_fin = 0
    
    def exorcism(attacking, defending):
        dmg = d4 * 2
        dmg_fin = defending.ap - dmg
        if dmg_fin < 0:
            dmg_fin = 0

    def mend(healer, healed):
        heal = healer.wp + d6
        healed.hp = healed.hp + heal


    for x in range(1,6): #Selects each character in order of initiative

        if atkorder[x] in enemy: #if selected character is an enemy just calculates its dmg
            chosen = random.choice[warrior, priest] #chooses randomly between the 2 allied characters to attack
            chosen.hp = chosen.hp - dmg_calc(atkorder[x])
            current_char = atkorder[x].name
            print(f"\nEnemy {current_char} attacked allied {chosen} and dealt {dmg_calc} damage.")
            ui()
            
        elif atkorder[x] in ally: #if selected character is an ally it enters the action screen
            print(f"It's time for {current_char} to do an action!\nWhat should {current_char} do?\nThe {current_char} can either Attack or cast Magic")
            action = input()

            if action in atk_words: #Attack action was chosen
                while check == 1:
                    print(f"Which enemy should {current_char} attack?")
                    atkenemy = input()
                    if atkenemy in enemy: #Checks if targeted character is an enemy
                        atkenemy.hp = dmg_calc(current_char, atkenemy)
                        print(f"The allied {current_char} attacked enemy {atkenemy} and dealt {dmg_calc} damage.")
                        check = 0
                    else:
                        print(f"\nChosen target not valid.\n")

            elif action in magic_words: #Magic action was chosen
                print(f"The {current_char} can cast the following magic:")
                while check == 1:
                    if current_char == warrior:  #checks if current character is a warrior
                        print(rushdown)
                        target = input(f"Who do you want to attack?\n")
                        if target in enemy: #checksif target is an enemy
                            rushdown(current_char, target)
                            check = 0
                        else:
                            print("Invalid target")
                    elif current_char == priest: #checks if current character is a priest
                        print(f"{exorcism}\n{mend}")
                        spell = input(f"Which spell do you want to use?\n")
                        if spell == "Exorcism" or spell == "exorcism":
                            target = f"Who do you want to attack?\n"
                            if target in enemy: #checks if target is an enemy
                                exorcism(current_char, target)
                                check = 0
                            else: 
                                print("Chosen target not valid.")
                        if spell == "Mend" or spell == "mend":
                            target = f"Who do you want to heal?\n"
                            if target in ally:  #checks if target is an ally
                                mend(current_char, target)
                                check = 0
                            else:
                                print("Chosen target not valid")
            else:
                print("The character cant do that action.")

        else:
            print("Something not intended happened.")
          
ui()
alive()