# Question 1
Alpha = 65
# @!_Charlie = 67
# 123_Alpha = 65
delta = 68
_bravo = 66
print(Alpha)
# print( @!_Charlie)
# print(123_Alpha)
print(delta)
print(_bravo)

# Question 2
"""end=primitive data type?
a. float
c. String
e. Boolean
h. Integer
"""

# Question 3
x = 0
while x < 10:
    x = x+1  # 1-small, 2-null, 3-4-medium, 5-6-medium, 7-8-medium, 9-10-medium, false
    if x == 1:
        print(x, "small")
    if x > 2:
        x = x+1
        print(x, "medium")
    if x == 5:
        x = 7
        print(x, "big")

# Question 4
a = 9.0
print(type(a))

# Question 5
my_tuple = (1, 2, 3, 4)
my_set = {1, 2, 3, 4}
print(my_tuple == my_set)

# Question 6
x = 10
if x < 11 and x > 9:
    print("if")
elif x > 10:
    print("elif")
else:
    print("else")

# Question 7
while True:
    print("True")
    break
    print("Break")
    break
    print("False")

# Question 8
x = 3
print(x)
while True:
    x = x-1
    if x == 1:
        continue
    elif x == 0:
        print("END")
        break
    else:
        print(x)

# Question 9
print(1 > 3 or 2 > 1)

# Question 10
x = 1+(0*10)*3/8**1
print(x)
