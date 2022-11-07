import random

class char_stats:
    def __init__(stat, hp, mp, ap, wp, init, d20):
        stat.hp = hp 
        stat.mp = mp 
        stat.ap = ap
        stat.wp = wp
        stat.init = init
        stat.roll = d20

warrior = char_stats(32, 5, 2, 5, 2, 0) #Warrior stats in order: HP, MP, AP, WP, Init, dice roll

priest = char_stats(20, 25, 0, 2, 6, 0) #Priest stats in order: HP, MP, AP, WP, Init, dice roll

orc = char_stats(15, 0, 2, 2, 2, 0) #Orc stats in order: HP, MP, AP, WP, Init, dice roll

goblin = char_stats(14, 0, 2, 2, 2, 0) #Goblin stats in order: HP, MP, AP, WP, Init, dice roll

hobgoblin = char_stats(13, 0, 2, 2, 2, 0) #Hobgoblin stats in order: HP, MP, AP, WP, Init, dice roll

kobold = char_stats(12, 0, 2, 2, 2, 0) #Kobold stats in order: HP, MP, AP, WP, Init, dice roll

enemy = [orc, goblin, hobgoblin, kobold] #list of enemy chars

ally = [warrior, priest] #list of allied chars

atk_words = ["atk","Atk", "attack", "Attack"]

magic_words = ["mag", "Mag", "magic", "Magic"]

rushdown = ["Rushes into the enemy, tackling them into the ground. Inflicts between 6 and 11 damage. Costs 5 mana."]

exorcism = ["Corrupt and enemy's life essence. Inflicts between 2 and 12 damage. Costs 5 mana."]

mend = ["Repay some of a character's current debt to the Death god. Heals a character between 3 and 8. Costs 3 mana."]

def ui(): #Basic ui (Might change later)
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
    chars = [warrior, priest, orc, gob, hob, kob]
    alive = []
    for char in chars:
        if char.hp > 0:
            alive.append(char)

def initiative(): #Rolls a dice for each character and sorts them in order of most to least initiative
    global atkorder

    def d20(): # Code based on answer by user jws1 on StackOverflow. (https://stackoverflow.com/questions/60193710/python-d20-dice-rolling-program)
        total = 0
        total += random.randint(1,20)

    for char in alive:
        char.d20 = d20() + char.init
        atkorder = sorted(alive, key=lambda h: (h.d20)) # Code based on answer by user falsetru on StackOverflow (https://stackoverflow.com/questions/26310394/python-sort-a-list-of-objects-based-on-their-attributes)

def Round(): #Gets a character from the initiative order and calculate's its actions.
    def dmg_calc(attacking, defending):
        dmg_fin = defending.ap - attacking.wp
        if dmg_fin < 0:
            dmg_fin = 0

    for x in range(1,6): #Selects each character in order of initiative

        if atkorder[x] in enemy: #if selected character is an enemy just calculates its dmg
            chosen = random.choice[warrior, priest] #chooses randomly between the 2 allied characters to attack
            chosen.hp = chosen.hp - dmg_calc(atkorder[x])
            print(f"\nEnemy {atkorder[x]} attacked allied {chosen} and dealt {dmg_calc} damage.")
            
        elif atkorder[x] in ally: #if selected character is an ally it enters the action screen
            print(f"It's time for {atkorder[x]} to do an action!\nWhat should {atkorder[x]} do?\nThe {atkorder[x]} can either Attack or cast Magic")
            action = input()

            if action in atk_words: #Attack action was chosen
                while check == 1:
                    print(f"Which enemy should {atkorder[x]} attack?")
                    atkenemy = input()
                    if atkenemy in enemy:
                        atkenemy.hp = dmg_calc(atkorder[x], atkenemy)
                        print(f"The allied {atkorder[x]} attacked enemy {atkenemy} and dealt {dmg_calc} damage.")
                        check = 0
                    else:
                        print(f"\nChosen target not valid\n")

            elif action in magic_words: #Magic action was chosen
                print(f"The {atkorder[x]} can cast the following magic:")
                while check == 1:
                    if atkorder[x] == warrior:
                        print(rushdown)
                    elif atkorder[x] == priest:
            else:
                print("The character cant do that action.")

        else:
            print("Something not intended happened.")
    
ui()
alive()
initiative()