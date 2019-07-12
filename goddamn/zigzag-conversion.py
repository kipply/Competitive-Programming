class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        ans = ["" for _ in range(numRows)]
        
        r = 0 
        d = "down"
        for i in range(n): 
            ans[r] += s[i] 
            if d is "down" and r == numRows - 1 and numRows == 1: 
                continue
            elif d is "down" and r == numRows - 1: 
                d = "up"
                r -= 1 
            elif d is "down": 
                r += 1 
            elif d is "up" and r == 0: 
                d = "down"
                r += 1 
            elif d is "up": 
                r -= 1 
        return("".join(ans))