state_capitals={"Washington":"Olympia",
                "Oregon":"Salem","California":"Sacramento"}
'''
#for-in loop
for state in state_capitals:
    print(state)    #key will printed


#dictionary method for values
for city in state_capitals.values():
    print(city)     #print values
'''

#iterating with both keys and values
for state in state_capitals:
    print(state_capitals[state], "is the capital of", state)

print()
for state, city in state_capitals.items():
    print(city, "is the capital of", state)