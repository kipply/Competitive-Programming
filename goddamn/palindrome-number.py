class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x) 
        n = len(s)
        for i in range(n // 2): 
            if s[i] != s[- i - 1]: 
                return False 
        return True