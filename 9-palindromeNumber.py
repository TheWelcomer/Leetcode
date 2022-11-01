def isPalindrome(self, x: int) -> bool:
    digits = 0
    testX = x
    flippedX = 0
    while testX != 0:
        digits += 1
        testX = testX // 10
    for i in range(digits):
        digit = x % pow(10, i)
        flippedX += digit * pow(10, digits - i)
    if x == flippedX:
        return True
    else:
        return False
    
print(isPalindrome(325, 323))