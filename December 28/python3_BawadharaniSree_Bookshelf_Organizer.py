def canOrganizeBooks(books, shelfSize):
    # Keep track of the current group size
    group_count = 0
    
    # Traverse through each book in the books array
    for i in range(len(books)):
        if group_count == 0:  # Start of a new shelf
            group_count += 1
        else:
            if books[i] == books[i-1] + 1:  # Continuation of a valid sequence
                group_count += 1
            else:
                return False
        
        # If a shelf is complete (group size matches shelfSize)
        if group_count == shelfSize:
            group_count = 0  # Reset for next shelf
    
    # If there are leftover books in a group, it's invalid
    return group_count == 0
