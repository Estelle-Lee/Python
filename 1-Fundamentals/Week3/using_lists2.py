states=["Washington","Oregon","California"]
"""
for state in states:
    state=state.lower()
    print(state)


print("Washington" in states)
print("Tennessee" in states)
print("Washington" not in states)

"""

# Concatenating Operations/lists
states2=["Arizona","Ohio","Louisina"]
best_states=states+states2
print(best_states)

# Slicing a Lists
# we use bracket notation and index numbers

#print index number 1, 2
print(best_states[1:3]) # 1 to 3 but not including index 3
#print index 0,1
print(best_states[:2])
#print index 4,5
print(best_states[4:])