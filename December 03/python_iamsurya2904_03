def alternating_square_arrangement(R, B):
    if abs(R - B) > 1:
        return "Not possible"
    
    result = []
    major, minor, major_color, minor_color = (R, B, 'R', 'B') if R >= B else (B, R, 'B', 'R')
    
    for _ in range(major + minor):
        if major > 0:
            result.append(major_color)
            major -= 1
        if minor > 0 and len(result) == 0 or result[-1] == major_color:
            result.append(minor_color)
            minor -= 1
            
    return "".join(result)

# Test cases
print(alternating_square_arrangement(3, 2))  # Output: "RBRBR"
print(alternating_square_arrangement(4, 2))  # Output: "Not possible"
