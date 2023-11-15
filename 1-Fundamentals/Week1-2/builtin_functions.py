"""print("Math Functions")

abs_int=abs(-1) #abs=absolute number
print(abs_int)

int_to_float=float(100) #float=floating point of value
print(int_to_float)

float_to_int=int(1.23)
print(float_to_int)

# if you want to use variable only once
print(int(2.25))

print(max(1,2,-5,10,0)) #max function takes multiple arguments: find the biggest number

print(min(1,2,-5,10,0))

print(pow(2,3)) #pow: power. 2 to the power of 3.

print(round(51.6))"""


# functions
"""def my_function():
    print("Hello from a function")  #creating

my_function()   # execute/call


def my_function(fname):
    print(fname+"Refsnes")

my_function("Email")
my_function("Tobias")
my_function("Linus")

# 2 arguments function
def my_function(fname, lname):
    print(fname+" "+lname)

my_function("Email","Refsnes")

#arbitrary arguments, *args
# when you do not know how many arguments that will be passed into your function, 
# add a * before the parameter name in the function definition. 
# This way the function will receive a tuple of arguments, 
# and can access the items accordingly
def my_function(*kids):
    print("The youngest child is "+kids[2])

my_function("Email","Tobias","Linus")

#keyword arguments
def my_function(child3, child2, child1):
    print("The youngest child is "+child3)

my_function(child1="Emil", child2="Tobias", child3="Linus")

#arbitrary keyword arguments, **kwargs
# if the number of keyword arguments is unknown,
# add a double ** before the parameter name
def my_function(**kid):
    print("His last name is "+kid["lname"])
my_function(fname="Tobias", lname="Refsnes")

# Default parameter value
def my_function(country="Norway"):
    print("I am from "+ country)

my_function("Sweden")
my_function("India")
my_function()   #prints default value
my_function("Brazil")

# passing a list as an argument
def my_function(food):
    for x in food:
        print(x)
fruits=["apple","banana","cherry"]
my_function(fruits)

# return values
def my_function(x):
    return 5*x

print(my_function(3))
print(my_function(5))
print(my_function(9))

# the pass statement
# to avoid getting an error of empty content
def myfunction():
    pass"""

# *******RECURSION
# function recursion: a defined function can call itself
# can loop through data to reach a result
# very efficient and mathematically-elegant approach
# ---Warnings---
# terminate!!!!
# excess amounts of memory
# excess amounts of processor power
def tri_recursion(k):
    if(k>0):
        result=k+tri_recursion(k-1)
        print(result)
    else:
        result=0
    return result

print("\n\nRecursion Example Results")
tri_recursion(6)