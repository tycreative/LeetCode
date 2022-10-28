def convert(s: str, numRows: int) -> str:
    length = len(s) # save length of s
    x = (numRows - 1) * 2 # x variable used for calculations
    indexes = [[] for _ in range(numRows)] # set up array of indexes for each row
    output = "" # variable used for output

    if numRows < 2: # quick check to just return s if only one row
        return s

    for r in range(numRows): # iterate through rows
        i = 1 # counter variable
        while (x * i) - (x - r) < length or (x * i) - r < length: # while calculated indexes are within boundaries
            indexes[r].append((x * i) - (x - r)) # save calculated indexes (these are the vertical column positions in the zig zag)
            if r != 0 and r != numRows - 1 and (x * i) - r < length: # don't need diagonal indexes for starting or ending row
                indexes[r].append((x * i) - r) # save calculated indexes (these are the diagonal positions in the zig zag)
            i += 1 # update counter

    for row in indexes:
        for i in row:
            output += s[i] # format output

    return output

assert convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
assert convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
