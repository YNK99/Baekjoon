class Solution(object):
    def isPalindrome(self, x):
        reverse_x = str(x)[::-1]
        if reverse_x == str(x):
            return True
        else:
            return False
        """
        :type x: int
        :rtype: bool
        """
        