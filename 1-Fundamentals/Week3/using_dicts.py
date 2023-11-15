state_capitals={"Washington":"Olympia",
                "Oregon":"Salem","California":"Sacramento"}
#print(len(state_capitals))

#print(state_capitals["Washington"])

#replace the value
state_capitals["Washington"]="Aberdeen"


#adding the value
state_capitals["Texas"]="Austin"

#different way to delete the value: 
#delete the value -1 using del
del state_capitals["California"]

#delete the value -2 using .pop()
#state_capitals.pop("Oregon")

removed_capital=state_capitals.pop("Oregon")
print(state_capitals)
print(removed_capital)