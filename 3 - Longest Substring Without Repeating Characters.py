def lengthOfLongestSubstring(s: str) -> int:
    length = len(s) # save length of string

    if length < 2: # quick check if length is less than 2
        return length # just return length

    if length == 2: # quick check if length is 2
        if s[0] == s[1]: # compare first char to last char
            return 1 # return 1 if same
        else:
            return 2 # otherwise return 2

    longest = 0 # variable for saving longest length, default of 0
    sub = {} # initialize dict for holding substrings
    start = end = 0 # initialize start and end variables to be 0
    
    while end < length: # repeat until end >= length
        if sub.get(s[end]): # if char in dict
            start = max(start, sub[s[end]]) # see if window should be moved

        longest = max(longest, end - start + 1) # see if longest should be updated
        sub[s[end]] = end + 1 # update or add to dict
        end += 1 # increment end
    return longest

assert lengthOfLongestSubstring("abcabcbb") == 3
assert lengthOfLongestSubstring("bbbbb") == 1
assert lengthOfLongestSubstring("pwwkew") == 3
assert lengthOfLongestSubstring("ab") == 2
