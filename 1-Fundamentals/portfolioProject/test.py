from math import sin,cos,radians
import random

club_force={"Driver":14,"Wood":10,"Iron7":8,"Wedge":5,"Putter":3}
#hit_time=random.randint(1,5)
hit_force=[0,1,2,3,4,5]  #hit force- do it random
# initial_velocity=[]
# if club is putter: angle 50,60,70 is accessible
# if club is wedge: angle 50,60 is accessible
# if club is iron: angle 50 is accessible
# every club is accessible to angle 20,30,40
# to avoid duplicate values, store angle values in set()
angle={20,30,40}
gravity=9.8
max_value=0.
min_value=0.
min_club=""
min_angle=0
max_club=""
max_angle=0
index=0

for club,force in club_force.items():
    for hitF in hit_force:
        velocity=force*hitF
        
        # initial_velocity.append(velocity)

        print("-----------Default setting-----------")
        print(f"Club choice: {club}")
        print(f"Power: {force}")
        print(f"Hit time: {hitF}")
        print(f"Velocity: {velocity}\n")

        if hitF==0:
            print("You didn't hit! Missed your turn")
        else:
            if index==2:
                angle.add(50)
            if index==3:
                angle.add(60)
            if index==4:
                angle.add(70)

            for angle_idx in angle:
                ball_angle=radians(angle_idx)

                t_flight=2*velocity*sin(ball_angle)/gravity
                hDistance=velocity*cos(ball_angle)*t_flight

                print(f"----- In {angle_idx}degree: Distance {round(hDistance,2)}m and flight time took {round(t_flight,2)}s")

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
    index += 1


               
                
print(f"Max distance: {round(max_value,2)} with {max_club} in angle {max_angle}, \nMin distance: {round(min_value,2)} with {min_club} in angle {min_angle}")
