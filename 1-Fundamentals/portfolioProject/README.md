# Project Title: Go-Fish text based game

## Introduction:

Play Go-fish text based game with opponent. You can play with another player, just enter your name and your opponent. 
Game runs for 5 round and if round finishes, you can choose to end game or restart the game. Experience speacial record breaking moment while play!

### Features:

- **Data set:**
I designed to have dictionaries to store the data of dice and allocated values. Additionally, string to temporarily store achievement and list inside the dictionary to store user name with allocated achievements. 

- **Implementing:**
Implement dictionaries of the angle while club has chosen. 
Append list of achievements inside the dictionaries.

## Design and Implementation

I designed to have same angles per club at the start, however, decided to add realistic fun facters: like world record; bonus points, did some research of golf clubs and found that more powerful club tends to hit low angle - and of course it is hard to play high angled shot with Driver - therefore modified the angle dictionary to initially have 3 keys and values. So the player who choses driver or wood will not able to select higher angle automatically. 
Additionally, I designed to have multiple class with super class for the goal_zone since there are 6 different zone with different lists of achievements stored. However, while finding allocating zone did not required super class. So I split one function to two for readability

### Instructions:
1. Enter terminal and run game file
>>> python game.py

2. Follow the screen and insert players name
>>> 
Before game start...
What is your name? Estelle
What is second player's name? Lee

3. Read the menu and choose your club
    a. Or type exit/q to quite the game

4. If choosed to quite, end_game() will run and print the score

5. If choosed a club, game starts

6. Automatically three dice will run and the player will receive hit force, wind force with direction, and angle of the club

7. The calculation is based on general force formula, however, in terms of the wind force, according to its direction, force can be increased by wind force or decreased by wind force.

8. When player1 plays, round score will be shown

9. Player switched automatically, so careful to check player's name on the screen

10. Each round, each player can select new club. Player can either choose same club or new club before hit.

11. After Round 5, game ends and shows final score of each players, achievements they got.
'''
==========================================================
======================= Game Over =======================

Estelle scores 0
Estelle achieves []
Anne scores 0
Anne achieves []
==========================================================

Wow, It's a tie!
'''

12. There is a speacial feature for players to experience, when the distance player had hit has break the record of guinness world record, the player will receive bonus points
>>>
!!!Bonus Points!!!
You broke the European Long Drive record!!!!!
Recognised by Guinness World Records as the European Long Drive Championship is 433m (473 yards) by Allen Doyle in September 2005

!!!More Bonus Points!!!
You broke the South African Long Drive record!!!!!
Recognised by Guinness World Records as the South African Long Drive Championship is 463m (506 yards) by Nico Grobbelaar in September 2012

!!!You did it! Mega Bonus Points!!!
You broke the world record!!!!!
Recognised by Guinness World Records as the longest drive in a competition is 471m (515 yards) by 64-year-old Mike Austin in 1974 at the US Senior National Open Qualifier with a 43.5” steel shafted persimmon wood driver

## Conclusion:

- **Code runs:** Code runs without error. 
- **Learned:** Various math functions used. Searched map() function for visualisation. Mastered dictionary data set.
- **Shortcomings:** 
- Currently users are only available for two only. It could be better to choose how many players will be from player itself and run even if there is only one player or 10+ players. Also current maximum game round is 5, however this could also be modified. If player plays solo game, it can decriment, while increase when there are many players - also would be good if player can select the maximum game round.
- Did not checked the overall runtime. It will required if there is large number of players or when game round increased. 
- I wanted to use Timer function and use it to provide players a remaining time for club selecting. And wanted to store the second for the hit power. Currently I designed random.randint(0,5) indicates 5 seconds. Currently, if hit power be 0, it indicates the player did not hit on time, while I want to implement this feature to 0 - weakest, 5 - strongest and when exceeding that provided 5 seconds, player loose the turn - did not hit on time. 
- **Future Plans:**
I want to add class for users to handle various number of players. And then will focus on implementing images so that the players can view their golf play - I think this can be done with map() function. And keep continously implement timer function to it.