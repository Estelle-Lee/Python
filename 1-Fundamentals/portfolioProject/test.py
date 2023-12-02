from math import sin,cos,radians
import random

club_force={"Driver":13,"Wood":10,"Iron7":8,"Wedge":5,"Putter":3}
#hit_time=random.randint(1,5)
hit_time=[0,1,2,3,4,5]
# initial_velocity=[]
# if club is putter: angle 50,60,70 is accessable
# if club is wedge: angle 50,60 is accessable
# if club is iron: angle 50 is accessable
# every club is accessable to angle 20,30,40
angle=[20,30,40,50,60,70]
gravity=9.8
max_value=0.
min_value=0.
min_club=""
min_angle=0
max_club=""
max_angle=0

for club,force in club_force.items():
    for time in hit_time:
        velocity=force*time
        # initial_velocity.append(velocity)

        print("-----------Default setting-----------")
        print(f"Club choice: {club}")
        print(f"Power: {force}")
        print(f"Hit time: {time}")
        print(f"Velocity: {velocity}\n")

        if time==0:
            print("You didn't hit! Missed your turn")
        else:
            for angle_idx in angle:
                ball_angle=radians(angle_idx)

                t_flight=2*velocity*sin(ball_angle)/gravity
                hDistance=velocity*cos(ball_angle)*t_flight

                print(f"----- In {angle_idx}: Distance {round(hDistance,2)}m and flight time took {round(t_flight,2)}s")

                if min_value==0:
                    min_value=hDistance
                
                if min_value>hDistance:
                    min_value=hDistance
                    min_angle=angle_idx
                    min_club=club

                if max_value<hDistance:
                    max_value=hDistance
                    max_angle=angle_idx
                    max_club=club

               
                
print(f"Max distance: {round(max_value,2)} with {max_club} in angle {max_angle}, \nMin distance: {round(min_value,2)} with {min_club} in angle {min_angle}")