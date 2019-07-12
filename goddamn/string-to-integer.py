 import re

 class Solution:
     def myAtoi(self, str: str) -> int:
         try: 
             ints = re.findall(r"^\s*[\+\-]?\d+", str)[0]
         except: return 0
         ans = int(ints)
         if ans < 0: 
             return max(-2147483648, ans)
         return min(2147483647, ans)
