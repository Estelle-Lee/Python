"""
Algorithm for Go Fish Game

Start Date: 10/11/2023
End Date:

"""
from math import sin,cos,radians
import random

# end_game(): call to end the game
# parameter: total_score
# return: none
def end_game(total_score):
    print("Your final score is ",total_score)
    print("Goodbye")


# game_menu(): Calls game menu and prompt user to choose club and return user's choice
# parameter: total_score
# return: custom_input: integer
def game_menu(total_score):
    custom_input=input("You can now select your golf club or type exit/q to quit").lower()
    total_score=total_score

    print("1) Driver")
    print("2) Wood")
    print("3) Iron 7")
    print("4) Wedge")
    print("5) Putter")

    if custom_input=='exit' or custom_input=='q':
        end_game(total_score)
    elif custom_input=='1' or custom_input=='2' or custom_input=='3' or custom_input=='4' or custom_input=='5':
        return int(custom_input)
    else:
        print("Invalid input. \sPlease choose valid club or exit/q to quit.")
        game_menu(total_score)

def find_goal_achievement(h):
    pass

# start_game(): call to start the game
# parameter: total_score, choice of club
# return: none
def start_game(total_score,chosen_club):
    # initial_velocity=float(input('Enter the initial velocity(m/s): '))
    # angle=float(input('Enter the angle of projection (degrees) '))
    initial_velocity=random.randint(1:6)
    angle=random.randint(1:6)

    print("Rolling the dices of your power...")
    print(f"Your power is {initial_velocity}!")
    print("Rolling the dices of the club angle...")
    print(f"Angle is {angle}!")

    t,h,v=calculate_distance(initial_velocity,angle)
    achievement,achievement_point=find_goal_achievement(h)
    print(f'Wow! You hit {achievement}! \sYou score {achievement_point}points!')
    print(f'Wow! Duration of Flight: {t}s')
    print(f'The Maximum horizontal distance traveled: {h}m')
    print(f'The Maximum vertical distance traveled: {v}m')

def drag_force():
    df=1
    return df

def calculate_distance(initial_velocity,angle):
    angle=radians(angle)
    gravity=9.8
    """
    velocity=math.sqrt(2)*height*weight
    energy=0.5*m*velocity**2
    mass=density*volumn=force/a
    volumn=4.3*math.pi*radius**3
    speed=g*time
    force=m*g
    density=mass/volumn
    drag=g*density*speed**2
    distance=0.5*g*t**2
    """
    windDragForce=random.randint(1,6)
    print("Dice rolled... Wind blows ",windDragForce)
    # flight time
    t_flight=2*initial_velocity*sin(angle)/gravity

    #x-coordinate
    hDistance=initial_velocity*cos(angle)*t_flight

    t=t_flight/2

    #y-coordinate: peak point
    vDistance=initial_velocity*sin(angle)*t-gravity/2*t**2

    return t_flight, hDistance, vDistance


if __name__=='__main__':
    total_score=0

    print("Welcome to Go Fish text-based Game!")

    chosen_club=game_menu(total_score)

    start_game(total_score,chosen_club)
    

    

    
    