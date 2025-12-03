#9. Check if number is Palindrome
#Leetcode username: shravani8_8

class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s==s[::-1]
        