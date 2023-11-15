import random

high_score = 0

def dice_game():
    global high_score

    while True:
        print(f"\nCurrent High Score:{high_score}")
        print("1) Roll Dice")
        print("2) Leave Game")
        user_choice=input("Enter your choice: ")
        print()
    
        #thrown
        if user_choice=='1':
            total=0

            for i in range(2):
                roll=random.randint(1,6)
                print(f"You roll a... {roll}")
                total+=roll

            print(f"\nYou have rolled a total of: {total}")

            if total>high_score:
                high_score=total
                print("\nNew high score!\n")
        elif user_choice=='2':
            print("Goodbye!")
            break
        else:
            print("Invalid input")

dice_game()
