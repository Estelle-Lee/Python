"""
Name: Bokyung Lee
Date: 04/11/2023

Task 1
set up the game variables: the game characters and their stats

Task 2
Prompt the player to choose from a list of options

Task 3
Set up infinite while loop to handle player choice

Task 4
Battle with the Dragon

Bonus Task 1
Give the player a choice to type in their character by name

Bonus Task 2
Case free

Bonus Task 3
Add 4th character "Orc"

Bonus Task 4
Add option to exit from the game entirely

Bonut Task 5
When the game is over, the player is asked if they want to play again.

"""
game=True

while game:
    wizard="Wizard"
    elf="Elf"
    human="Human"
    orc="Orc"

    wizard_hp=70
    elf_hp=100
    human_hp=150
    orc_hp=170

    wizard_damage=150
    elf_damage=100
    human_damage=20
    orc_damage=110

    dragon_hp=300
    dragon_damage=50

    while game:
        print("\n1)\t",wizard,"\n2)\t",elf,"\n3)\t",human,"\n4)\t",orc,"\n5)\t Exit")
        character=input("Choose your character: ").lower()
        
        if character=='1' or character=='wizard':
            character=wizard
            my_hp=wizard_hp
            my_damage=wizard_damage
            break
        if character=='2' or character=='elf':
            character=elf
            my_hp=elf_hp
            my_damage=elf_damage
            break
        if character=='3' or character=='human':
            character=human
            my_hp=human_hp
            my_damage=human_damage
            break
        if character=='4' or character=='orc':
            character=orc
            my_hp=orc_hp
            my_damage=orc_damage
            break
        if character=='exit' or character=='5':
            game=False
            print("Game Over")
            break
        print("Unknown character")


    while game:
        print("You have chosen the character:",character,"\nHealth:",my_hp, "\nDamage:",my_damage)
        
        dragon_hp-=my_damage
        print("\nThe",character,"damaged the Dragon!")
        print("The Dragon's hitpoints are now:",dragon_hp)

        if dragon_hp<=0:
            print("\nThe Dragon has lost the battle")
            break

        my_hp-=dragon_damage
        print("\nThe Dragon strikes back at",character)
        print("The",character,"'s hitpoints are now:",my_hp)

        if my_hp<=0:
            print("\nThe",character,"has lost the battle")
            break

    play_again=input("Play again? (y/n): ").lower()
    if play_again=='n':
        print("Goodbye")
        break