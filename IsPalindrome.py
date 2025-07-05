class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False  # Negative numbers are not palindromes

        s = str(x)
        for i in range(len(s) // 2):
            if s[i] != s[len(s) - 1 - i]:
                return False
        return True
