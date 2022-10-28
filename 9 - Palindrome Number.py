def isPalindrome(x: int) -> bool:
    if str(x) == str(x)[::-1]: # convert x to str and compare it to reversed self
        return True # return true if palindrome
    return False # otherwise false

assert isPalindrome(121) is True
assert isPalindrome(-121) is False
assert isPalindrome(10) is False
