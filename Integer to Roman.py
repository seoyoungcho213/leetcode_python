# https://leetcode.com/problems/integer-to-roman
# Time complexity : O(1)
# Space complexity : O(1)

class Solution:
    def intToRoman(self, num: int) -> str:
        digit = num % 10
        result = ""

        # 1
        result = self.printDigit(digit, 'I', 'V', 'X', result)

        # 10
        digit = (num // 10) % 10
        result = self.printDigit(digit, 'X', 'L', 'C', result)

        # 100
        digit = (num // 100) % 10
        result = self.printDigit(digit, 'C', 'D', 'M', result)

        # 1000
        digit = num // 1000
        while digit:
            result += 'M'
            digit -= 1

        return result[::-1]

    def printDigit(self, digit: int, one: str, five: str, ten: str, result: str) -> str:
        if(digit == 4) :
            result = result + five + one
            return result
        if(digit == 9) :
            result = result + ten + one
            return result
       
        flag = 1 if digit >= 5 else 0
        if(flag): digit -= 5
        while digit:
            result += one
            digit -= 1
        
        if(flag): result += five
        return result
