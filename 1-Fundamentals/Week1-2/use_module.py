# don't need to provide extension name of the file. 
# only needs the name
"""
import my_module

my_module.greet("Albert Einstein")
print("My favorite ice cream flovour is", my_module.flavour)

"""
# This can save memories by only import what we want to use
from my_module import greet, flavour

greet("Albert Einstein")
print("My favorite ice cream flovour is", flavour)