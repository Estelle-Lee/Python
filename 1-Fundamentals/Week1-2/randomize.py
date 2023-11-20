import random

"""pips=random.randint(1,6)
print("You roll the die... it lands with",pips,"pips showing.")

# , will add a space
# + will not add a space
prizes=["a car","$10000","a pony","$500000"]
prize_won=random.choice(prizes)
print("You turn the wheel of fortune... It lands on a prize of", prize_won+"!!")

cards=[1,2,3,4,5,6,7,8,9,10,11]
random.shuffle(cards)
print("The cards are now in this order: ")
print(cards)"""

# velocity=[30,20,10,-10,-20,-30]
# random_velocity=random.choice(velocity)
# print(random_velocity)

wind_dict={1:30,2:20,3:10,4:-10,5:-20,6:-30}
angle_dict={1:20,2:30,3:40,4:50,5:60,6:70}

dice_wind=random.randint(1,6)
is_wind_forward='forward'
if wind_dict[dice_wind]<0:
    is_wind_forward='backward'

dice_angle=random.randint(1,6)

print('Rolling a dice...')
print(f"You roll {dice_wind} for wind and its' value is {is_wind_forward} {abs(wind_dict[dice_wind])}m/s")

print('Rolling another dice for...')
print(f"You roll {dice_angle} for angle and its' value is {angle_dict[dice_angle]}degree")

'''
want to pick one number from 1 to 6, 
and tell player a number and allocated value. 
    << can I find the key based on value from the dictionary? I don't want to store a value from the dice. but how to print without storing?
and store the value to use in calculation.


print()
print(initial_velocity,angle)
'''