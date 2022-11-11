import random, os

class char_stats:
    def __init__(stat, name, hp, mp, ap, wp, init, d20):
        stat.name = name
        stat.hp = hp 
        stat.mp = mp 
        stat.ap = ap
        stat.wp = wp
        stat.init = init
        stat.d20 = d20

warrior = char_stats("warrior", 32, 5, 2, 5, 2, 0) #Warrior stats in order: Name, HP, MP, AP, WP, Init, dice roll

priest = char_stats("priest", 20, 25, 0, 2, 6, 0) #Priest stats in order: Name, HP, MP, AP, WP, Init, dice roll

orc = char_stats("orc", 15, 0, 2, 2, 2, 0) #Orc stats in order: Name, HP, MP, AP, WP, Init, dice roll

goblin = char_stats("goblin", 14, 0, 2, 2, 2, 0) #Goblin stats in order: Name, HP, MP, AP, WP, Init, dice roll

hobgoblin = char_stats("hobgoblin", 13, 0, 2, 2, 2, 0) #Hobgoblin stats in order: Name, HP, MP, AP, WP, Init, dice roll

kobold = char_stats("kobold", 12, 0, 2, 2, 2, 0) #Kobold stats in order: Name, HP, MP, AP, WP, Init, dice roll

enemy = ("orc","goblin", "hobgoblin", "kobold") #Tuple of enemy chars

ally = ("warrior", "priest") #Tuple of allied chars

atk_words = ["atk","Atk", "attack", "Attack"]

magic_words = ["mag", "Mag", "magic", "Magic"]

rush_desc = ["Rushdown: Rushes into the enemy, tackling them into the ground. Inflicts between 6 and 9 damage. Costs 5 mana."]

exor_desc = ["Exorcism: Corrupt and enemy's life essence. Inflicts between 2 and 8 damage. Costs 5 mana."]

mend_desc = ["Mend: Repay some of a character's current debt to the Death god. Heals a character between 3 and 8. Costs 3 mana."]

def ui(): #Basic ui (Might change later)
    clearconsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    clearconsole()

    print("Enemy: Orc            Enemy: Goblin           Enemy: Hobgoblin           Enemy: Kobold")
    print(f"HP:{orc.hp}                 HP:{goblin.hp}                   HP:{hobgoblin.hp}                      HP:{kobold.hp}")
    print(f"MP:{orc.mp}                  MP:{goblin.mp}                    MP:{hobgoblin.mp}                       MP:{kobold.mp}")
    print(f"AP:{orc.ap}                  AP:{goblin.ap}                    AP:{hobgoblin.ap}                       AP:{kobold.ap}")
    print(f"WP:{orc.wp}                  WP:{goblin.wp}                    WP:{hobgoblin.wp}                       WP:{kobold.wp}")
    print(f"Init:{orc.init}                Init:{goblin.init}                  Init:{hobgoblin.init}                     Init:{kobold.init}")

    print(f"\n\n\n\n\n")
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
        atkorder = alive
        atkorder.sort(key=lambda x: (x.d20), reverse = True) # Code based on answer by user Art on StackOverflow (https://stackoverflow.com/questions/67750705/python-sorting-based-on-class-attribute)

def Round(): #Gets a character from the initiative order and calculates its actions.
    def dmg_calc(attacking, defending):
        dmg_fin = attacking.wp - defending.ap
        if dmg_fin < 0:
            dmg_fin = 0
        return int(dmg_fin)

    def answer_into_character(ans): #this function converts a character's name into it's variable so the dmg_calc and spell functions can work
        if ans == "priest":
            return priest
        elif ans == "warrior":
            return warrior
        elif ans == "orc":
            return orc
        elif ans == "goblin":
            return goblin
        elif ans == "kobold":
            return kobold
        elif ans == "hobgoblin":
            return hobgoblin

    def d4():
        total = 0
        total += random.randint(1,4)
        return total

    def d6():
        total = 0
        total += random.randint(1,6)
        return total

    def rushdown(attacking, defending):
        dmg = attacking.wp + d4()
        dmg_fin = defending.ap - dmg
        if dmg_fin < 0:
            dmg_fin = 0
    
    def exorcism(defending):
        dmg = d4() * 2
        dmg_fin = defending.ap - dmg
        if dmg_fin < 0:
            dmg_fin = 0

    def mend(healer, healed):
        heal = healer.wp + d6()
        healed.hp = healed.hp + heal

    num_char = -1 #This refers to the caracter in the list of characters in order of initiative and goes up by one for each character

    for char in atkorder: #Selects each character in order of initiative
        num_char += 1 
        name_char = atkorder[num_char].name #gets the character name so the rest of the code can identify which character it is refering to

        if name_char in enemy: #if selected character is an enemy just calculates its dmg
            chosen = random.choice((warrior, priest)) #chooses randomly between the 2 allied characters to attack
            chosen.hp = chosen.hp - dmg_calc(char, chosen)
            print(f"\nEnemy {name_char} attacked allied {chosen.name} and dealt {dmg_calc(char, chosen)} damage.")
            
        elif name_char in ally: #if selected character is an ally it enters the action screen
            check = 1 # this check exists so the code can know when an allied character has finished its turn
            while check == 1:
                print(f"It's time for the {name_char} to do an action!\nWhat should the {name_char} do?\nThe {name_char} can either Attack or cast Magic")
                action = input()
                if action in atk_words: #Attack action was chosen
                        atkenemy = input(f"Which enemy should {name_char} attack?\n")
                        if atkenemy in enemy: #Checks if targeted character is an enemy
                            atkenemy = answer_into_character(atkenemy)
                            atkenemy.hp = dmg_calc(char, atkenemy)
                            print(f"The allied {name_char} attacked enemy {atkenemy.name} and dealt {dmg_calc(char, atkenemy)} damage.")
                            check = 0
                        else:
                            print(f"\nChosen target not valid.\n")

                elif action in magic_words: #Magic action was chosen
                    print(f"The alied {name_char} can cast the following magic:")
                    while check == 1:

                        if char == warrior:  #checks if current character is a warrior
                            print(rush_desc)
                            target = input(f"Who do you want to attack?\n")
                            if target in enemy: #checks if target is an enemy
                                target = answer_into_character(target)
                                rushdown(char, target)
                                check = 0
                            else:
                                print("Invalid target")

                        elif char == priest: #checks if current character is a priest
                            print(f"{exor_desc}\n{mend_desc}")
                            spell = input(f"Which spell do you want to use?\n")
                            if spell == "Exorcism" or spell == "exorcism":
                                target = input(f"Who do you want to attack?\n")
                                if target in enemy: #checks if target is an enemy
                                    target = answer_into_character(target)
                                    exorcism(target)
                                    check = 0
                                else: 
                                    print("Chosen target not valid.")
                            elif spell == "Mend" or spell == "mend":
                                target = input(f"Who do you want to heal?\n")
                                if target in ally:  #checks if target is an ally
                                    target = answer_into_character(target)
                                    mend(char, target)
                                    check = 0
                                else:
                                    print("Chosen target not valid")
                else:
                    print("The character cant do that action.")

        else:
            print("Something not intended happened.")
ui()
alive()
initiative()
Round()
