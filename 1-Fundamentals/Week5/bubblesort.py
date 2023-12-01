unsorted_list=[101,49,3,12,56]

def bubblesort(the_list):
    #maximum comparison should be number of items -1
    high_idx=len(the_list)-1

    # the number of json pairs == highest list index
    for i in range(high_idx):
        list_changed=False
        for j in range(high_idx):
            item=the_list[j]
            next=the_list[j+1]

            if item>next:   #swap
                the_list[j]=next
                the_list[j+1]=item
                list_changed=True
            
            print(the_list,i,j)
        print(list_changed)
        if list_changed==False:
            break

bubblesort(unsorted_list)