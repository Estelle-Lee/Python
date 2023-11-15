# Bokyung
# 13/11/2023

import random

diamonds=["AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand=[]

while diamonds:
    userChoice=input("\nPick a card by entering OR Q to quit: ").lower()

    if userChoice=='q':
        break
    else:
        selectedIndex=random.randint(0,len(diamonds)-1)

        hand.append(diamonds[selectedIndex])
        diamonds.pop(selectedIndex)
        
        print("You picked: ",hand)
        print("Remaining cards: ",diamonds)
        

#if diamonds list is empty
if not diamonds:
    print("\nThere are no more cards to pick")


