class Solution(object):
    def longestPalindrome(self, s):
        n = len(s)

        ans_n = 1
        ans_str = ""

        def expand(s, i, j): 
          while s[i] == s[j] and i != 0 and j < len(s) - 1: 
            i -= 1 
            j += 1
          if s[i] != s[j]:
            return (j - i - 1, s[i + 1:j]) 
          else:
            return (j - i + 1 , s[i:j + 1]) 

        for i in xrange(n - 1): 
          attempt = expand(s, i, i)
          
          if s[i] == s[i + 1]: 
            attempt = expand(s, i, i + 1)
            if attempt[0] > ans_n: 
                ans_n = attempt[0]
                ans_str = attempt[1] 
          elif attempt[0] > ans_n: 
            ans_n = attempt[0]
            ans_str = attempt[1] 

        if s and not ans_str: 
            ans_str = s[0]
        return ans_str