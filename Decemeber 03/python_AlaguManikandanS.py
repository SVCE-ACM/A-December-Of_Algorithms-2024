def arrange_squares(R, B):
    if abs(R - B) > 1:
        return "Not possible"
    
    result = ""
    while R > 0 or B > 0:
        if R >= B:  
            result += 'R' 
            R -= 1
        if B > 0:  
            result += 'B' 
            B -= 1

    return result

print(arrange_squares(5, 4))  
print(arrange_squares(4, 2))  
