my_string="alpha"
'''
multiline_string="""bravo
charlie"""
print(my_string)
print(multiline_string)


print(my_string[0])
print(my_string[3])

print(my_string[0:3])   #0,1,2
print(my_string[:2])    #0,1
print(my_string[2:])

#my_string[0]=='b'   #not available.

#for loop
for char in my_string:
    print(char)
'''

print("pha" in my_string)
print("z" not in my_string)
print(my_string[0])
if my_string[0]=='a' or my_string[0]=='d' or my_string[0]=='e' or my_string[0]=='f':
    print("working")
else:
    print("dumm")
