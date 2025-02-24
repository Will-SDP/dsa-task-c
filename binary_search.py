def binary_search(item, item_list):
    #Get the list size 
    list_size = len(item_list) -1 
    # Start at the two ends of the list 
    lower_idx = 0 
    upper_idx = list_size 

    while lower_idx <= upper_idx:
        
        # TODO calculate the middle point 
        mid_point = (lower_idx + upper_idx) // 2 
        #print(mid_point)
        #print(f"Mid ping: {mid_point}")

        # TODO if the item is found return the index 
        if item_list[mid_point] == item:
            return mid_point

        # TODO otherwise get the next midpoing 
        if item > item_list[mid_point]:
            lower_idx = mid_point + 1 
        else:
            upper_idx = mid_point -1     

    if lower_idx > upper_idx:
        return None 