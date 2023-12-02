"""
Should be a text-based game.

Idea 1: text based battle adventure game - finding way to exit with options of movement.
    Character 1: Player
    Character 2: NPC
    Sets: Strength=10/Agility=10/Luck=10/HP=10/Defence=10
    Story line: 
        If Player moves best route from choosing [left, right, forward], 
            no battle, 
            Player gain Luck +1,
            Player gain HP +1
        If Player moves normal route, 
            no battle
        If Player moves and meet NPC, then start the battle of three stage
            Player can move: Attack/Defence
            If Player attack and success
                Player gain Agility +2
                Player gain Luck +1
                Player loose HP -1
                NCP loose Strength -2
                NCP loose HP-2
                NCP loose Defence -2
            If Player attack and fails
                Player loose HP -2
                Player loose Agility -2
                Player loose Luck -1
                NCP gain Agility +1
                NCP gain Defence +1
                NCP loose HP -1
            If Player attack and even
                Player loose HP -1
                NCP loose HP -1
            If Player defence and success
                Player gain Agility +2
                Player gain Defence +2
                Player gain Luck +1
                Player loose HP -1
                NCP loose strength -2
                NCP loose Agility -2
                NCP loose HP -2
            ...
            Overall, if Player wins more than twice,
                Player gain Strength +2
            if Player loose more than twice,
                Player loose strength -2
        If Luck<10 and Luck>5:
            Choice of the route contains normal route and NCP route only.
        If Luck<=5:
            Only NCP route is available.
        If Luck>=10 and Luck<14:
            Choice of the route contains best route, normal route, and NCP route.
        If Luck>=14 and Luck<16:
            Choice of the route contains best route and normal route
        If Luck>=16:
            Only best route is available.
        If HP==0:
            Game Lose
        If travel ends success, Player wins.


                




Idea 2: Hangman
Idea 3: Tic-tac-toe
Idea 4: Golf base fishing game
    [velocity, force, angle, Distance]
    F=ma
    s=vt
    Earth worm hit
        -> Bomb...
    Island: Boots, Tin, Tuna Can 
        -> 1 points
    Cheap stage: Clownfish (Nemo), Shellfish
        -> 5 points
    Medium stage: Wahoo
        -> 30 points
    Valuable stage: Shark, Beluga whale, Killer whale
        -> 200 points
    Most Valuable stage: Humpback whale
        -> 500 points


implementation plan:
OOP approach:
work:
"""
