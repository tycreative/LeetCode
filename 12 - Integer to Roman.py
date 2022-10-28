def intToRoman(num: int) -> str:
    integers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1] # integers array
    romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"] # roman numerals array
    roman = "" # output variable
    i = 0 # counter variable

    while i < 13: # iterate thru 13 integers
        while num >= integers[i]: # while number can fit integer
            roman += romans[i] # update output
            num -= integers[i] # subtract from number
        i += 1 # increment counter
    return roman

assert intToRoman(3) == "III"
assert intToRoman(58) == "LVIII"
assert intToRoman(1994) == "MCMXCIV"
