class Solution:
    def romanToInt(self, s: str) -> int:
        s_list = list(s)
        roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        res = 0

        for ind in range(len(s)):
            if ind < len(s)-1 and roman[s[ind]] < roman[s[ind+1]]:
                res -= roman[s[ind]]
            else:
                res += roman[s[ind]]
        return res
        
        
        


            

        