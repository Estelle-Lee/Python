def reverse(str):
    #should use slicing notation
    return str[::-1]    #means start at the end of the string and end at position 0, move with the step -1, negative one, which means one step backwards

name = input("What is your name? ")
print("Your name reversed is:", reverse(name))
