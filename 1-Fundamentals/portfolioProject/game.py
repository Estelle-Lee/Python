"""
Algorithm for Go Fish Game

Start Date: 10/11/2023
End Date: 02/12/2023

"""
from math import sin,cos,radians
import random

game_round=1
total_score=0
user_database={}
player1_score=0
player2_score=0


# end_game(): call to end the game
# parameter:
# return: none
def end_game():
    print()
    print("==========================================================")
    print("======================= Game Over =======================\n")
    print(f"{user1} scores {player1_score}")
    print(f"{user1} achieves {user_database[user1]}")
    print(f"{user2} scores {player2_score}")
    print(f"{user2} achieves {user_database[user2]}")
    print("==========================================================")
    print()
    if player1_score<player2_score:
        print(f"\nCongratulations {user2} Won!")
    elif player1_score==player2_score:
        print(f"Wow, It's a tie!")
    else:
        print(f"\nCongratulations {user1} Won!")

    print("\n\nGoodbye")

    
# goal_zone(): called by find_goal_achievement()
# parameter: total_distance: float
# return: achievement: string, point: integer
def goal_zone(total_distance):
    zone1_items=['Bomb']
    zone2_items=['Boots','Tin','Tuna Can']
    zone3_items=['Clownfish','Shellfish','Mickey Mouse Platy','Zebrafish']
    zone4_items=['Wahoo','Tuna','Salmon']
    zone5_items=['Shark','Beluga Whale','Killer Whale']
    zone6_items=['Humpback whale']

    point=0
    print()

    if total_distance>=0.5 and total_distance<30:
        print("Ooh, Worm cast")
        achievement=random.choice(zone1_items)
    if total_distance>=30 and total_distance<100:
        print("You reached to a small pond!")
        achievement=random.choice(zone2_items)
        point=1
    if total_distance>=100 and total_distance<206:
        print("You reached to a rock island")
        achievement=random.choice(zone3_items)
        point=5
    if total_distance>=206 and total_distance<279:
        print("You reached to a river!")
        achievement=random.choice(zone4_items)
        point=30
    if total_distance>=279 and total_distance<326:
        print("You goaled to the ocean!")
        achievement=random.choice(zone5_items)
        point=200
    if total_distance>=326:
        print("You goaled to the deep DEEP ocean!")
        achievement=random.choice(zone6_items)
        point=500

    return achievement,point


# find_goal_achievement(): called by start_game()
# parameter: total_distance: float
# return: achievement: string, point: integer
def find_goal_achievement(total_distance):
    bonus_point=100

    achievement,point=goal_zone(total_distance)
    
    if total_distance>433:
        print("\n!!!Bonus Points!!!")
        print("You broke the European Long Drive record!!!!!")
        print("Recognised by Guinness World Records as the European Long Drive Championship is 433m (473 yards) by Allen Doyle in September 2005")
        point+=bonus_point

    if total_distance>463:
        print("\n!!!More Bonus Points!!!")
        print("You broke the South African Long Drive record!!!!!")
        print("Recognised by Guinness World Records as the South African Long Drive Championship is 463m (506 yards) by Nico Grobbelaar in September 2012")
        point+=bonus_point
            
    if total_distance>471:
        print("\n!!!You did it! Mega Bonus Points!!!")
        print("You broke the world record!!!!!")
        print("Recognised by Guinness World Records as the longest drive in a competition is 471m (515 yards) by 64-year-old Mike Austin in 1974 at the US Senior National Open Qualifier with a 43.5” steel shafted persimmon wood driver")
        point+=bonus_point

    return achievement,point


# calculate_distance(): called by start_game()
# parameter: velocity: float, angle:integer
# return: -1:break, distance: integer
def calculate_distance(velocity,angle):
    angleR=radians(angle)
    gravity=9.8


    if velocity<0.:
        return -1
    else:
        # flight time
        t_flight=2*velocity*sin(angleR)/gravity

        #x-coordinate
        hDistance=velocity*cos(angleR)*t_flight

        t=t_flight/2

        #y-coordinate: peak point
        vDistance=velocity*sin(angleR)*t-gravity/2*t**2

        print("\n====HIT STATUS====")
        print("Distance:", round(hDistance,2),"m")
        print("Flight time:", round(t_flight,2),"s")
        print("Vertical distance:", round(vDistance,2),"m")

        return hDistance
    

# print_scores(): called by next_turn()
# parameter: none
# return: none
def print_scores():
    print(f"============ Round {game_round} ============")
    for userName,achievements in user_database.items():
        print(f"{userName}: {achievements}")
        print("Score:",player1_score if userName==user1 else player2_score)


# next_turn(): called by start_game()
# parameter: current_player:string
# return: none
def next_turn(current_player):
    global total_score, player1_score, player2_score, game_round

    if user_database[current_player] !="" or user_database[current_player]!=[]:
        if current_player==user1:
            player1_score+=total_score
            total_score=0

            print_scores()
            game_menu(user2)
        else:
            player2_score+=total_score
            total_score=0
            if game_round==5:
                print_scores()
                end_game()
            else:
                game_round+=1
                print_scores()
                game_menu(user1)


# start_game(): call to start the game
# parameter: player:string, chosen_club: string, club_force: int
# return: none
def start_game(player,chosen_club,club_force):
    global total_score, user_database
   
    print(f"\n--Round {game_round}: {player} with {chosen_club}!\n")
    
    # Dice concept of velocity and angle
    wind_dict={1:30,2:20,3:10,4:0,5:-10,6:-20}
    angle_dict={1:20,2:30,3:40}

    hit_force=random.randint(0,5)
    print('Rolling a dice...')
    print(f"You roll {hit_force} for hit force")
    if hit_force==0:
        print("You didn't hit! Missed your turn")
        next_turn(player)
    
    dice_wind=random.randint(1,6)
    is_wind_forward='forward'
    if wind_dict[dice_wind]<0:
        is_wind_forward='backward'
    print('Rolling a dice...')
    print(f"You roll {dice_wind} for wind and its' value is {is_wind_forward} {abs(wind_dict[dice_wind])}m/s")

    # if club is putter: angle 50,60,70 is accessible
    # if club is wedge: angle 50,60 is accessible
    # if club is iron: angle 50 is accessible
    # every club is accessible to angle 20,30,40
    print('Rolling a dice...')
    if chosen_club=='Driver' or chosen_club=='Wood':
        dice_angle=random.randint(1,3)
    else:
        angle_dict[4]=50
        if chosen_club=='Iron7':
            dice_angle=random.randint(1,4)
        else:
            angle_dict[5]=60
            if chosen_club=='Wedge':
                dice_angle=random.randint(1,5)
            else:
                angle_dict[6]=70
                dice_angle=random.randint(1,6)
    print(f"You roll {dice_angle} for angle and its' value is {angle_dict[dice_angle]} degree")

    velocity=(club_force*hit_force)+wind_dict[dice_wind]
    
    # call calculation function
    distance=calculate_distance(velocity,angle_dict[dice_angle])

    if distance<0:
        print("Bad luck. You hit the ground")
        achievement=""
        point=0
    else:
        achievement,point=find_goal_achievement(distance)
        print()
        if point==0:
            print(f"{player} found {achievement}.\nCheer up =)")
        else:
            print(f"{player} found {achievement}\nYour earned {point} points")

    user_database[player].append(achievement)
    total_score+=point

    next_turn(player)


# game_menu(): Calls game menu and prompt user to choose club and return user's choice
# parameter: player: string
# return: null
def game_menu(player):
    print(f"\n{player} Please choose your club:")
    print("1) Driver")
    print("2) Wood")
    print("3) Iron 7")
    print("4) Wedge")
    print("5) Putter\n")

    custom_input=input("You can now select your golf club or type exit/q to quit ")     
    
    club_force={"Driver":13,"Wood":10,"Iron7":8,"Wedge":5,"Putter":3}

    if custom_input in 'exitExitqQ':
        end_game()
    elif custom_input in 'driver1DriverDRIVER':
        key='Driver'
    elif custom_input in 'wood2WoodWOOD':
        key='Wood'
    elif custom_input in 'ironIronIRON3':
        key='Iron7'
    elif custom_input in 'wedgeWedgeWEDGE4':
        key='Wedge'
    elif custom_input in 'putterPutterPUTTER5':
        key='Putter'    
    else:
        print("Invalid insert\nPlease try again")
        game_menu(player)

    start_game(player,key,club_force[key])


# Driver function
if __name__=='__main__':
    user1=input("Before game start...\nWhat is your name? ")       
    user2=input("What is second player's name? ")
    user_database[user1]=[]
    user_database[user2]=[]

    print("\n===========Welcome to Go Fish text-based Game!===========")
    game_menu(user1)

    

    
    