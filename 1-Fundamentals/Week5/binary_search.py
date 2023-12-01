def binary_search(the_list,target):
    # find lower bound : index
    lower_bound=0
    upper_bound=len(the_list)-1

    # set a loop
    # while loop 
    while lower_bound<=upper_bound:
        #floor division 5//2=2
        pivot=(lower_bound+upper_bound)//2

        pivot_value=the_list[pivot]

        if pivot_value==target:
            return pivot
        
        if pivot_value>target:
            upper_bound=pivot-1
        else:
            lower_bound=pivot+1

    # if the target is not in the list
    return -1


my_list=[1,2,3,4,5,6,7,8,9,10]
print(binary_search(my_list,10))
print(binary_search(my_list,4))
print(binary_search(my_list,33))