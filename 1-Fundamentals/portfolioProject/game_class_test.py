"""
Algorithm for Go Fish Game

Start Date: 10/11/2023
End Date:

"""
from math import sin,cos,radians
import random

round=1
total_score=0
achievement=[]
user_database={}

class User():
    def __init__(self,name,score,achievement):
        self.name=name
        self.score=score
        self.achievement=achievement

class gameUser(User):
    # end_game(): call to end the game
    # parameter: total_score
    # return: none
    def end_game(total_score):
        print("Your final score is ",total_score)
        print("Goodbye")


    def find_goal_achievement(total_distance):
        zone1_items=['Bomb']
        zone2_items=['Boots','Tin','Tuna Can']
        zone3_items=['Clownfish','Shellfish','Mickey Mouse Platy','Zebrafish']
        zone4_items=['Wahoo','Tuna','Salmon']
        zone5_items=['Shark','Beluga Whale','Killer Whale']
        zone6_items=['Humpback whale']

        point=0
        bonus_point=100
        if total_distance>=0.5 and total_distance<30:
            print("Ooh, Worm cast")
            print(f"You found {zone1_items()}\nYour earned {point} points")
            return zone1_items(),point
        if total_distance>=30 and total_distance<100:
            achievement_index=random.randint(len(zone2_items)-1)
            gained_point=1
            point+=gained_point
            print("You reached small pond!")
            print(f"You found {zone2_items[achievement_index]}\nYour earned {gained_point} points")
            return zone2_items[achievement_index],point
        if total_distance>=100 and total_distance<206:
            achievement_index=random.randint(len(zone3_items)-1)
            gained_point=5
            point+=gained_point
            print("You reached rock island")
            print(f"You found {zone3_items[achievement_index]}\nYour earned {gained_point} points")
            return zone3_items[achievement_index],point
        if total_distance>=206 and total_distance<279:
            achievement_index=random.randint(len(zone4_items)-1)
            gained_point=30
            point+=gained_point
            print("You reached river!")
            print(f"You found {zone4_items[achievement_index]}\nYour earned {gained_point} points")
            return zone4_items[achievement_index],point
        if total_distance>=279 and total_distance<326:
            achievement_index=random.randint(len(zone5_items)-1)
            gained_point=200
            point+=gained_point
            print("You reached ocean!")
            print(f"You found {zone5_items[achievement_index]}\nYour earned {gained_point} points")
            return zone5_items[achievement_index],point
        if total_distance>=326:
            gained_point=500
            point+=gained_point
            print("You reached deap ocean!")
            print(f"You found {zone6_items()}\nYour earned {gained_point} points")

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


            return zone6_items(),point


    def calculate_distance(velocity,angle):
        angleR=radians(angle)
        gravity=9.8

        
        # flight time
        t_flight=2*velocity*sin(angleR)/gravity

        #x-coordinate
        hDistance=velocity*cos(angleR)*t_flight

        t=t_flight/2

        #y-coordinate: peak point
        vDistance=velocity*sin(angleR)*t-gravity/2*t**2
        
        print("\nWoW\nThis is your ball status!")
        print(f"Distance: {round(hDistance,2)}m")
        print(f"Flight time: {round(t_flight,2)}s")
        print(f'Vertical distance: {round(vDistance,2)}m')

        prize,point=find_goal_achievement(hDistance)
        achievement.append(prize)
        total_score+=point
        return total_score
        

    def next_turn(current_player):
        for user in user_database.keys():
            if current_player!=user:
                game_menu(user)

    # start_game(): call to start the game
    # parameter: chosen_club: string
    #           club_force: int
    # return: none
    def start_game(player,chosen_club,club_force):
    
        print(f"\n--Round {round} begins!\n")
        
        # Dice concept of velocity and angle
        wind_dict={1:30,2:20,3:10,4:-10,5:-20,6:-30}
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
        if chosen_club.lower()=='driver' or chosen_club.lower()=='wood':
            dice_angle=random.randint(1,3)
        else:
            angle_dict[4]=50
            if chosen_club.lower()=='iron7':
                dice_angle=random.randint(1,4)
            else:
                angle_dict[5]=60
                if chosen_club.lower()=='wedge':
                    dice_angle=random.randint(1,5)
                else:
                    angle_dict[6]=70
                    dice_angle=random.randint(1,6)
        print(f"You roll {dice_angle} for angle and its' value is {angle_dict[dice_angle]} degree")

        velocity=club_force*hit_force+wind_dict[dice_wind]

        # call calculation function
        score=calculate_distance(velocity,angle_dict[dice_angle])
        user_database[player]=score
        next_turn(player)

    # game_menu(): Calls game menu and prompt user to choose club and return user's choice
    # parameter: 
    # return: 0 / -1
    def game_menu(player):
        try:
            isFirst=True
            for score in user_database.values():
                if score!=0:
                    isFirst=False
            
            if isFirst==False:
                round+=1

            print("\nPlease choose your club:")
            print("1) Driver")
            print("2) Wood")
            print("3) Iron 7")
            print("4) Wedge")
            print("5) Putter\n")

            custom_input=input("You can now select your golf club or type exit/q to quit").lower()       
            
            club_force={"Driver":13,"Wood":10,"Iron7":8,"Wedge":5,"Putter":3}

            if custom_input=='exit' or custom_input=='q':
                end_game(total_score)
                
            
            if custom_input.find('1') or custom_input.find('driver'):
                key='Driver'
            if custom_input.find('2') or custom_input.find('wood'):
                key='Wood'
            if custom_input.find('3') or custom_input.find('iron'):
                key='Iron7'
            if custom_input.find('4') or custom_input.find('wedge'):
                key='Wedge'
            if custom_input.find('5') or custom_input.find('putter'):
                key='Putter'    

            start_game(player,key,club_force[key])

        except TypeError:
            print("Type Error")
            print("Try again")
            game_menu(player)

        except ValueError:
            print("Value Error")
            print("Try again")
            game_menu(player)

# Driver function
if __name__=='__main__':
    try:
        user1=input("Before game start,,,\nWhat is your name? ")       
        user2=input("What is Player2's name? ")
        user_database[register(user_database,user1)]=0
        user_database[register(user_database,user2)]=0

        print("===========Welcome to Go Fish text-based Game!===========")
        game_menu(user1)
    except TypeError:
        pass
    except ValueError:
        pass

    # call start_game function
    # return it's value to total_score
    # achievement,achievement_point=start_game(chosen_club)
    

    

    
    