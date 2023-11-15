# W3Schools - Python For Loop
# this for loop does not require an indexing variable to set beforehand.
fruits=["apple","banana","cherry"]
"""for x in fruits:
    print(x)

# Looping Through a String
for x in "banana":
    print(x)

# The break statement
for x in fruits:
    print(x)
    if x=="banana":
        break

for x in fruits:
    if x=="banana":
        break
    print(x)

# The continue statement
for x in fruits:
    if x=="banana":
        continue
    print(x)"""

# The range() function
# The range() function returns a sequence of numbers,
# starting from 0 by default, 
# and increments by 1 (by default),
# and ends at a specified number
"""for x in range(6):
    print(x)

for x in range(2,6):
    print(x)

for x in range(2,30,3):
    print(x)"""

# Else in For Loop
# print all numbers, 
# and print Else phrase when the loop has ended
"""for x in range(6):
    print(x)
else:
    print("Finally finished!")"""

# else block will not be executed if the loop is stopped by a break statement.
"""for x in range(6):
    if x==3: break
    print(x)
else:
    print("Finally Finished!")"""

# Nested Loops
"""adj=["red", "big", "tasty"]
fruits=["apple","banana","cherry"]

for x in adj:
    for y in fruits:
        print(x,y)"""

# The pass Statement
# since for loops cannot be empty, 
# but if you for some reason have a for loop with no content, 
# put in the pass statement to avoid getting an error.
"""for x in [0,1,2]:
    pass"""

"""fruits=["apple","banana","cherry"]
for x in fruits:
    print(x)"""

# create a function named my_function
"""def my_function():
    print("Hello from a function")
my_function() # execute a function named my_function"""

# W3Schools - Python If ... Else
a=33
b=200
if b>a:
    print("1. b is greater than a")
elif a==b:
    print("1. a and b are equal")
else:
    print("1. a is greater than b")

# short hand if
if a>b: print("2. a is greater than b")

# short hand if...else
a=2
b=330
print("3. A") if a>b else print("3. B")

a=330
b=330
print("4. A") if a>b else print("4. =") if a==b else print("4. B")

a=200
b=33
c=500
if a>b and c>a:
    print("5. Both conditions are True")

if a<b or a>c:
    print("6. At least one of the conditions is True")

a=33
b=200
if not a>b:
    print("7. a is not greater than b")

x=41
if x>10:
    print("8. Above ten,")
    if x>20:
        print("and also above 20!")
    else:
        print("but not above 20.")

if b>a:
    pass