states=["Washington","Oregon","California"]

"""
print(states[-1])
print(states[-2])
print(states[-3])
"""

states[2]="Arizona"
#print(states)
#print(len(states))    # len(): length

states.append("New York")   #add at the very end
print(states)

states.pop()   # if we call pop with no argument, it will remove or pop off the very last item of the list
print(states)

states.pop(1)   # if we call pop with specific index number, it will removed.
print(states)