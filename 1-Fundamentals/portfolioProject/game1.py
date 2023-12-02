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


def find_goal_achievement(h):
    pass


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


# def drag_force():
#     df=1
#     return df

# start_game(): call to start the game
# parameter: choice of club
# return: none
def start_game(chosen_club):
    # initial_velocity=float(input('Enter the initial velocity(m/s): '))
    # angle=float(input('Enter the angle of projection (degrees) '))

    # Dice concept of velocity and angle
    wind_dict={1:30,2:20,3:10,4:-10,5:-20,6:-30}
    angle_dict={1:20,2:30,3:40,4:50,5:60,6:70}

    dice_wind=random.randint(1,6)
    is_wind_forward='forward'
    if wind_dict[dice_wind]<0:
        is_wind_forward='backward'

    dice_angle=random.randint(1,6)

    # -- Dice roll --
    print('Rolling a dice...')
    print(f"You roll {dice_wind} for wind and its' value is {is_wind_forward} {abs(wind_dict[dice_wind])}m/s")

    print('Rolling another dice for...')
    print(f"You roll {dice_angle} for angle and its' value is {angle_dict[dice_angle]}degree")

    # call calculation function
    t,h,v=calculate_distance(wind_dict[dice_wind],angle_dict[dice_angle])

    # call achievement function
    achievement,achievement_point=find_goal_achievement(h)

    # show result
    print(f'Wow! You hit {achievement}! \sYou score {achievement_point}points!')
    print(f'Wow! Duration of Flight: {t}s')
    print(f'The Maximum horizontal distance traveled: {h}m')
    print(f'The Maximum vertical distance traveled: {v}m')

    return achievement,achievement_point




# game_menu(): Calls game menu and prompt user to choose club and return user's choice
# parameter: 
# return: custom_input: integer
def game_menu():

    print("1) Driver")
    print("2) Wood")
    print("3) Iron 7")
    print("4) Wedge")
    print("5) Putter\s")

    # further challenge 1: prompt user to enter the value within 5 seconds. print counting from terminal.
    # further challenge 2: if player enter valid value within 5 seconds, check the second and store to initial_velocity
    # further challenge 3: then return game_menu() function with custom_input and initial_velocity
    custom_input=input("You can now select your golf club or type exit/q to quit").lower()



    if custom_input=='exit' or custom_input=='q':
        end_game(total_score)
        return -1
    elif custom_input=='1' or custom_input=='2' or custom_input=='3' or custom_input=='4' or custom_input=='5':
        return int(custom_input)
    else:
        print("Invalid input. \sPlease choose valid club or exit/q to quit.")
        return 0



# Driver function
if __name__=='__main__':
    
    total_score=0

    print("===========Welcome to Go Fish text-based Game!===========")

    # call game_menu function
    # return it's value to chosen_club
    chosen_club=game_menu()

    # call start_game function
    # return it's value to total_score
    achievement,achievement_point=start_game(chosen_club)
    

    

    
    