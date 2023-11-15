"""
Declaring Variables
"""
x = 12.2
y = 7
z = 9.0

print(x)
print(y)
print(z)

"""
primitive data types
integer: any whole number, 
float: any decimal number, 
string: sequence of characters enclosed in quotes, 
boolean: special value that can only be True or False
"""

name = "Bob"
age = 35
cash = 100.25
retired = False

# How to know the Data type of a variable
# Invoking the function 'type(<VARIABLE NAME>)'
print("Data type of the variable 'name' is", type(name))
print("Data type of the variable 'age' is", type(age))
print("Data type of the variable 'cash' is", type(cash))
print("Data type of the variable 'retired' is", type(retired))


"""
Composite data types

Data structures composed of one or more items stored in a single variable
Items can be of different data types and are comma separated

List: ordered sequence of multiple values
Dictionary: Unordered collection of key-value pairs
Tuple: similar to a list, but immutable
Set: unordered collection of immutable, unique values
"""
# Storing a List
nucamp_locations = ["Seattle", "Tacoma", "Bellevue"]

# Storing a Dictionary
Bob_Info = {"name": "Bob", "age": 35, "cash": 100.25, "retired": False}

# Storing a Tuple
my_tuple = ("apple", "bannana", "cherry")

# Storing a Set
my_set = {"cats", "dogs", "birds"}

print("Data type of the variable 'nucamp_locations' is", type(nucamp_locations))
print("Data type of the variable 'Bob' is", type(Bob_Info))
print("Data type of the variable 'my_tuple' is", type(my_tuple))
print("Data type of the variable 'mu_set' is", type(my_set))


"""
Multi-line Comments
"""

# Single-line Comments
