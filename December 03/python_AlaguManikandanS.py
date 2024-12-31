def arrange_squares(R, B):
    if abs(R - B) > 1:
        return "Not possible"
    
    result = []
    red = 'R'
    blue = 'B'
    
    if R > B:
        primary, secondary = red, blue
    else:
        primary, secondary = blue, red

    while R > 0 or B > 0:
        if R > 0 and (len(result) == 0 or result[-1] != red):
            result.append(red)
            R -= 1
        elif B > 0 and (len(result) == 0 or result[-1] != blue):
            result.append(blue)
            B -= 1
        else:
            return "Not possible"
    
    return "".join(result)

print(arrange_squares(3, 2)) 
print(arrange_squares(4, 2)) 
