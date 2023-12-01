def linear_search_dictionary(the_dic,target):
    for key in the_dic.keys():
        if the_dic[key]==target:
            print("Found at key",key)
            return the_dic[key]
    print("Target is not in the dictionary")
    return -1

my_dictionary = {"red": 5, "blue": 3, "yellow": 12, "green": 7}
linear_search_dictionary(my_dictionary, 5)
linear_search_dictionary(my_dictionary, 3)
linear_search_dictionary(my_dictionary, 8)