
# Inventory Implementation. Be add after the final version.

inventory = ["Health Potion", "Mana Potion", "Revival Item"]

print ("Oh right! Before you start fighitng, you can also use some items in your inventory to help your character's status in combat!（ミ￣ー￣ミ）")
print ("I will quickly show you your available items then.")

def freq(str):
    print()
    str_list = str.split()
    unique_words = set(str_list)
    for words in unique_words :
        print( str_list.count(words))
if __name__ == "__main__":
     
    str = ["Health Potion", "Mana Potion", "Revival Item"]
    freq(str)


