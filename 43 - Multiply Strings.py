# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(self.strInt(num1) * self.strInt(num2))

    def strInt(self, num, res = 0):
        for char in num:
            res = res * 10 + ord(char) - ord('0')
        return res

assert Solution().multiply("64", "2") == "128"
assert Solution().multiply("0", "1293832923") == "0"
assert Solution().multiply("5", "10") == "50"
