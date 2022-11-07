class char_stats:
    def __init__(stat, hp, mp, ap, wp, init):
        stat.hp = hp 
        stat.mp = mp 
        stat.ap = ap
        stat.wp = wp
        stat.init = init

warrior = char_stats(32, 5, 2, 5, 2) #Warrior stats in order: HP, MP, AP, WP, Init

priest = char_stats(20, 25, 0, 2,6) #Priest stats in order: HP, MP, AP, WP, Init

orc = char_stats(15, 0, 2, 2,2) #Orc stats in order: HP, MP, AP, WP, Init
