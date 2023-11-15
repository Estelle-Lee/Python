"""
my_string="giraffe"
print(my_string[-1])    #print "e": last character
print(my_string[2:4])   #print sublist of index 2,3: "ra"

b="Hello, World!"
print(b[-5:-2])
"""
list=[30,45,20,15,60]

sizeOfList=len(list)    #5

# reverse
end=(sizeOfList*-1)-1   #-6: to prevent excludings from for loop range
start=-1
for i in range(start, end, -1):
    # print each element using negative indexes
    print('list[{}]={}'.format(i,list[i]))

# OR
print(list[::-1])

# Setting a step
myStr="Thisisit. I did it! :)"
print("String = ",myStr)
end=(len(myStr)*-1)
print("String after slicing (negative indexing)= ",myStr[end:start:2])

