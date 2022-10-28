
def findSubstring(s: str, words: [str]) -> [int]:
    string = len(s) # length of string
    length = len(words[0]) # length of first word
    size = length * len(words) # size of all words (sample size)
    words = sorted(words) # sort words for later
    indexes = [] # initialize index array

    x = 0 # counter variable / index
    while x < (string - size) + 1: # while in sample size range
        if sorted([s[i:i+length] for i in range(x, size + x, length)]) == words: # split sample into array of length words, sort array, and compare
            indexes.append(x) # update indexes array
        x += 1 # increment counter
    return indexes

            
assert findSubstring("barfoothefoobarman", ["foo", "bar"]) == [0,9]
assert findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"]) == []
assert findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]) == [6,9,12]
