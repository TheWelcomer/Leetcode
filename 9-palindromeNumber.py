class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x < 0):
            return False
        digits = 0
        testX = x
        flippedX = 0
        while testX != 0:
            digits += 1
            testX = testX // 10
        for i in range(digits):
            digit = x % pow(10, i + 1)
            digit = digit // pow(10, i)
            flippedX += digit * pow(10, digits - i - 1)
        if x == flippedX:
            return True
        else:
            return False
