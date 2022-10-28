def longestPalindrome(s: str) -> str:
    length = len(s) # save length of s
    longest = s[0] # default of first char
    pals = {(i,i): 1 for i in range(length)} # set up dictionary for later (diagonally based)

    for i in range(length - 1, -1, -1): # iterate through string starting from end
        for j in range(i + 1, length): # iterate through string starting from i
            if s[i] == s[j] and (j - i == 1 or pals.get((i+1,j-1)) != None): # if two chars are equal check dict relationship
                pals[(i,j)] = 1 # update dict
                if len(s[i:j+1]) > len(longest): # update longest if necessary
                    longest = s[i:j+1]
    return longest

assert longestPalindrome("faacakbdacaab") == "aca"
assert longestPalindrome("banana") == "anana"
assert longestPalindrome("babad") == "aba"
assert longestPalindrome("cbbd") == "bb"
