class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        z = str(x)
        # Remove all whitespace and convert to lowercase
        s = z.replace(' ', '').lower()
        # Check if the string is the same as its reverse
        return s == s[::-1]