'''# single attribute class
class Player:
    max_hp=4000

#instantiate an object
#should not be indented; should be outside of the class
player1=Player()
print(player1.max_hp)

player2=Player()
print(player2.max_hp)

#two type of attribute: class attribute and instance attribute
#change the class attribute value
#less used
Player.max_hp=5000
print(player1.max_hp)
print(player2.max_hp)
'''
#instance attribute
class Player:
    #constructor method
    #used to declare and initialise instance attributes
    #instance attributes are stored per instance, rather than on the class
    #when you change an instance attribute, it does not affect the other instances
    #must have a parameter list,
    #***and the first parameter will always refer to the object being instantiated
    def __init__(self,name,hp):
        self.name=name
        self.hp=hp
        self.score=0

player1=Player("Aaron",1200)
player2=Player("Irene",1300)

print("Player1:",player1.name," -- HP:",player1.hp," -- SCORE:",player1.score)
print("Player2:",player2.name," -- HP:",player2.hp," -- SCORE:",player2.score)

player1.hp+=500
player1.score+=10
print("Player1:",player1.name," -- HP:",player1.hp," -- SCORE:",player1.score)
print("Player2:",player2.name," -- HP:",player2.hp," -- SCORE:",player2.score)