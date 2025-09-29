"""
9- Palindrome number

https://leetcode.com/problems/palindrome-number/

Given an integer x, return true if x is a palindrome, and false otherwise.
"""

# First solution
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        copy_x = x
        result = 0
        if x < 0: 
          return False
        while copy_x != 0:
          result = result * 10 + copy_x % 10
          copy_x //= 10
        return result == x


# Second solution
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
          return False
        return str(x) == str(x)[::-1]
