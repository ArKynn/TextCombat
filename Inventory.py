
# Inventory Implementation. To be add after the final version.

print ("Oh right! Before you start fighitng, you can also use some items in your inventory to help your character's status in combat!（ミ￣ー￣ミ）")
print ("I will quickly show you your available items.")
print()

def freq(str): #Based on Code Python3 (https://www.geeksforgeeks.org/find-frequency-of-each-word-in-a-string-in-python/)
    unique_words = set(str)

    for words in unique_words:
        print('You have', str.count(words), words)
if __name__ == "__main__":
    str = "Bonus Damage Item (+2)", "Mana Potion (+10)", "Revival Item", "Whistle"
 
    freq(str)
    print()

    print("That's all, not much but we are short on budget. However, you can find out what the whistle does later on.")


