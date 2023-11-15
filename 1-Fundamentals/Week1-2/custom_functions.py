# Custom functions 
# don't requires return value with the return statement

def myFn():
    print("You have called my function")

def add(x,y):
    z=x+y
    print(z)

myFn()
add(2,3)
add(3,4)

a=4
b=5
add(a,b)

"""def functionname(parameters):
    "function_docstring"
    function_suite
    return [expression]"""
def greetings():
    "This is docstring of greetings function"
    print("Hello World")
    return

greetings()

# Function definition is here
def printme(str):
    "This prints a passed string into this function"
    print(str)
    return

# No you can call printme function
printme("I'm first call to user defiend function")
printme("again")

def testfunction(arg):
    print("ID inside the function: ",id(arg))

var="Hello"
print("ID before passing: ", id(var))
testfunction(var)


def testfunction(arg):
    print("ID inside the function: ",id(arg))
    arg+=1
    print("new object after increment",arg,id(arg))

var=10
print("\nID before passing: ", id(var))
testfunction(var)
print("value after function call",var)


def testfunction(arg):
    print("inside the function: ",arg)
    print("ID inside the function: ",id(arg))
    arg=arg.append(100)

var=[10,20,30,40]
print("\nID before passing: ", id(var))
testfunction(var)
print("value after function call",var)


def greetings(name):
    "This is docstring of greetings function"
    print("\nHello {}".format(name))
    return
greetings("Samay")
greetings("Pratima")
greetings("steven")


def add(x,y):
    z=x+y
    return z
a=10
b=20
result=add(a,b)
print("\na={} b={} a+b={}".format(a,b,result))