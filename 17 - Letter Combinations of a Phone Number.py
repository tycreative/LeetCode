letters = { # possible letters of each digit
  "2": "abc", "3": "def", "4": "ghi",
  "5": "jkl", "6": "mno", "7": "pqrs", 
  "8": "tuv", "9": "wxyz"
}

def letterCombinations(digits: str) -> [str]:
    if digits == "": # quick check that digits are provided
        return [] # otherwise return empty array
    
    combos = [*letters[digits[0]]] # initialize combos array to chars of first digit (from dict) 
    for digit in digits[1:]: # iterate through remaining digits
        combos = [combo + letter for letter in letters[digit] for combo in combos] # generate combinations and update array
    return combos # return combinations

assert letterCombinations("23") == ['ad', 'bd', 'cd', 'ae', 'be', 'ce', 'af', 'bf', 'cf']
assert letterCombinations("") == []
assert letterCombinations("2") == ["a","b","c"]
